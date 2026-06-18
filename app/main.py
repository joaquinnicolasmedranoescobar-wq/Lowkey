from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from app.core.config import get_settings
from app.db.session import get_database_session
from app.routers import parts, orders, dashboard, expenses, maintenances, vehicles

# Datos de ejemplo para productos de automoción (adaptados al schema de la colección parts)
SAMPLE_PRODUCTS = [
    {
        "name": "Disco de freno Brembo Xtra (Delantero)",
        "description": "Disco de freno perforado y ranurado de alto rendimiento. Mejora la disipación del calor y la evacuación de agua, ideal para conducción deportiva.",
        "category": "frenos",
        "brand": "Brembo",
        "price": 149.99,
        "stock": 12,
        "compatibility": "VW Golf VII (1.2/1.4/2.0 TSI)",
        "reference": "BRK-BREM-XTRA-G7",
        "image": "https://example.com/images/brembo_xtra.jpg",
        "specs": {"tipo": "Perforado y ranurado", "medida": "312x25 mm", "posicion": "Delantero"}
    },
    {
        "name": "Pastillas de freno Bosch (Juego 4 piezas)",
        "description": "Pastillas de freno de cerámica con bajo nivel de polvo y ruido. Cumplen con la normativa ECE R90, alta durabilidad.",
        "category": "frenos",
        "brand": "Bosch",
        "price": 39.95,
        "stock": 25,
        "compatibility": "BMW Serie 3 (E90/E91/E92)",
        "reference": "BRK-BOSCH-PAD-E90",
        "image": "",
        "specs": {"material": "Cerámica", "normativa": "ECE R90"}
    },
    {
        "name": "Amortiguador Bilstein B6 Sport",
        "description": "Amortiguador de gas monotubo de alto rendimiento. Ofrece mayor estabilidad y control en curvas sin perder confort.",
        "category": "suspensión",
        "brand": "Bilstein",
        "price": 189.00,
        "stock": 8,
        "compatibility": "Audi A4 (B8 / 8K)",
        "reference": "SUS-BIL-B6-B8",
        "image": "https://example.com/images/bilstein_b6.jpg",
        "specs": {"tipo": "Gas monotubo", "posicion": "Eje delantero"}
    },
    {
        "name": "Kit de embrague Sachs Performance",
        "description": "Kit de embrague deportivo con disco orgánico y plato de presión reforzado. Soporta más par motor que el original (hasta +30%).",
        "category": "transmisión",
        "brand": "Sachs",
        "price": 359.99,
        "stock": 5,
        "compatibility": "Ford Focus ST (MK3 / 2.0 EcoBoost)",
        "reference": "TRN-SAC-PERF-FOCUS",
        "image": "",
        "specs": {"par_maximo": "500 Nm", "tipo": "Orgánico deportivo"}
    },
    {
        "name": "Kit de distribución Gates (Correa + Tensor)",
        "description": "Kit completo de distribución con correa de alta resistencia, tensor hidráulico y bomba de agua (opcional). Sustitución cada 120.000 km.",
        "category": "motor",
        "brand": "Gates",
        "price": 129.90,
        "stock": 15,
        "compatibility": "Opel Astra J / Insignia A (1.6/1.8/2.0 CDTI)",
        "reference": "ENG-GATES-KIT-ASTRA",
        "image": "https://example.com/images/gates_distribution.jpg",
        "specs": {"incluye": "Correa, tensor, rodillo", "kilometraje": "120.000 km"}
    },
    {
        "name": "Bujías NGK Iridium IX (Pack 4 uds.)",
        "description": "Bujías de iridio que proporcionan una chispa más potente y duradera. Mejoran la combustión y el rendimiento del motor.",
        "category": "motor",
        "brand": "NGK",
        "price": 49.99,
        "stock": 30,
        "compatibility": "Seat León Cupra / VW Golf GTI (EA888 Gen 3)",
        "reference": "ENG-NGK-IRI-CUPRA",
        "image": "",
        "specs": {"material": "Iridio", "calor": "8", "gap": "0.8 mm"}
    },
    {
        "name": "Filtro de aceite Mann-Filter",
        "description": "Filtro de aceite de alto flujo con tecnología de microfiltración. Retiene partículas de hasta 20 micras.",
        "category": "motor",
        "brand": "Mann-Filter",
        "price": 12.50,
        "stock": 50,
        "compatibility": "Mercedes-Benz Clase C (W204/S204)",
        "reference": "ENG-MANN-OIL-W204",
        "image": "",
        "specs": {"eficiencia": "99.5%", "tipo": "Cartucho"}
    },
    {
        "name": "Batería Varta Silver Dynamic 70Ah",
        "description": "Batería de arranque con tecnología AGM (Absorbent Glass Mat). Ideal para vehículos con Start/Stop y alta demanda eléctrica.",
        "category": "eléctrico",
        "brand": "Varta",
        "price": 149.00,
        "stock": 10,
        "compatibility": "Universal (Medidas: 278x175x190mm)",
        "reference": "ELE-VARTA-AGM70",
        "image": "https://example.com/images/varta_agm.jpg",
        "specs": {"capacidad": "70 Ah", "tecnologia": "AGM", "CCA": "760 A"}
    },
    {
        "name": "Faro Bi-Xenón Hella (Lado Izquierdo)",
        "description": "Faro delantero con proyectores bixenón, guía de luz LED diurna y nivelación automática. Incluye balasto y lámpara D1S.",
        "category": "eléctrico",
        "brand": "Hella",
        "price": 399.99,
        "stock": 4,
        "compatibility": "BMW X5 (E70 / LCI)",
        "reference": "ELE-HELLA-XENON-E70",
        "image": "",
        "specs": {"tipo": "Bi-Xenón", "balasto": "Incluido", "lado": "Izquierdo"}
    },
    {
        "name": "Brazos de suspensión delanteros Febi Bilstein (Par)",
        "description": "Juego de 2 brazos transversales con rótulas y silentblocks integrados. Restaura la geometría y estabilidad del tren delantero.",
        "category": "suspensión",
        "brand": "Febi Bilstein",
        "price": 189.95,
        "stock": 7,
        "compatibility": "VW Passat B7 / CC",
        "reference": "SUS-FEBI-CONTROL-B7",
        "image": "https://example.com/images/febi_control_arm.jpg",
        "specs": {"incluye": "2 brazos completos", "material": "Acero forjado"}
    },
    {
        "name": "Neumático Michelin Pilot Sport 5 (225/40 R18)",
        "description": "Neumático deportivo de altas prestaciones. Excelente agarre en seco y mojado, con gran durabilidad y respuesta en curva.",
        "category": "ruedas",
        "brand": "Michelin",
        "price": 179.90,
        "stock": 20,
        "compatibility": "Montaje universal (18 pulgadas, 5x112/5x114.3)",
        "reference": "WHE-MICH-PS5-22540R18",
        "image": "",
        "specs": {"medida": "225/40 R18", "indice_velocidad": "Y", "indice_carga": "92"}
    },
    {
        "name": "Llantas de aleación OZ Racing Hyper GT HLT 18\"",
        "description": "Llantas de aluminio forjado en tecnología HLT (High Light Technology). Muy ligeras y rígidas, ideales para uso deportivo.",
        "category": "ruedas",
        "brand": "OZ Racing",
        "price": 450.00,
        "stock": 6,
        "compatibility": "5 tornillos / 5x112 / ET45 / Centro 57.1",
        "reference": "WHE-OZ-HGT-18-BK",
        "image": "https://example.com/images/oz_hypergt.jpg",
        "specs": {"medida": "18x8J", "peso": "9.2 kg", "color": "Gris mate"}
    },
    {
        "name": "Silencioso trasero Akrapovič (Slip-On)",
        "description": "Silencioso deportivo fabricado en titanio con punta de carbono. Ofrece un sonido profundo y reduce el peso respecto al original.",
        "category": "escape",
        "brand": "Akrapovič",
        "price": 1899.00,
        "stock": 2,
        "compatibility": "Porsche 911 (992 / Carrera S)",
        "reference": "EXH-AKRA-SLIP-992",
        "image": "",
        "specs": {"material": "Titanio", "homologacion": "ECE", "peso": "-3.5 kg vs original"}
    },
    {
        "name": "Radiador de motor Nissens",
        "description": "Radiador de aluminio de alta eficiencia con núcleo mejorado. Asegura una refrigeración óptima en condiciones extremas.",
        "category": "motor",
        "brand": "Nissens",
        "price": 119.99,
        "stock": 9,
        "compatibility": "Toyota Corolla (E120 / E150)",
        "reference": "ENG-NISSEN-RAD-COROLLA",
        "image": "https://example.com/images/nissens_radiator.jpg",
        "specs": {"material": "Aluminio", "grosor": "32 mm", "incluye": "Tapón de llenado"}
    },
    {
        "name": "Pinza de freno TRW (Trasera) - Unidad",
        "description": "Pinza de freno flotante reconstruida de fábrica. Incluye pastillas y soporte, garantía de 2 años.",
        "category": "frenos",
        "brand": "TRW",
        "price": 149.50,
        "stock": 8,
        "compatibility": "Ford Fiesta ST (MK7 / MK7.5)",
        "reference": "BRK-TRW-CALIPER-FIESTA",
        "image": "",
        "specs": {"posicion": "Trasera derecha", "tipo": "Flotante", "incluye": "Pastillas"}
    },
    {
        "name": "Intercooler Forge Motorsport",
        "description": "Intercooler de carga frontal de gran tamaño (600x300x100mm). Reduce la temperatura del aire de admisión hasta un 30% para ganar potencia constante.",
        "category": "motor",
        "brand": "Forge Motorsport",
        "price": 699.00,
        "stock": 3,
        "compatibility": "Audi S3 / VW Golf R (8V / 5F)",
        "reference": "ENG-FORGE-IC-S3",
        "image": "https://example.com/images/forge_intercooler.jpg",
        "specs": {"volumen": "18 L", "presion_max": "4 bar", "incluye": "Tuberías de silicona"}
    }
]

settings = get_settings()
app = FastAPI(
    title=settings.api_title,
    description=settings.api_description,
    version=settings.api_version,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar el frontend (carpeta frontend/)
frontend_dir = os.path.join(os.path.dirname(__file__), "..", "frontend")
if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")
else:
    print("⚠️  Carpeta 'frontend/' no encontrada. Sirviendo solo la API.")

# Incluir routers
app.include_router(vehicles.router, prefix=settings.api_v1_prefix)
app.include_router(maintenances.router, prefix=settings.api_v1_prefix)
app.include_router(expenses.router, prefix=settings.api_v1_prefix)
app.include_router(dashboard.router, prefix=settings.api_v1_prefix)
app.include_router(parts.router, prefix=settings.api_v1_prefix)
app.include_router(orders.router, prefix=settings.api_v1_prefix)

# Semilla de productos (opcional)
@app.on_event("startup")
def seed_parts():
    db = get_database_session()
    if db.parts.count_documents({}) == 0:
        # Insertar productos de ejemplo
        for p in SAMPLE_PRODUCTS:
            db.parts.insert_one(p)
        print("✅ Productos de ejemplo insertados en la base de datos.")

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "Backend running and MongoDB Atlas connection initialized."}