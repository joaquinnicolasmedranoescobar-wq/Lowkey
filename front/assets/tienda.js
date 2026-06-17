const PRODUCTS = [
  // MOTOR
  { id:1,  emoji:'⚙️',  name:'Correa de distribución',       brand:'Gates',   ref:'K015693XS',     cat:'motor',        price:89.90,  oldPrice:null,   stock:'in',  compat:['Golf Azul','Seat León'],                  isNew:false, specs:{Material:'EPDM reforzado', Ancho:'22mm',        Dientes:152,   Garantía:'2 años'} },
  { id:2,  emoji:'🛢️',  name:'Filtro de aceite',             brand:'Bosch',   ref:'F026407006',    cat:'filtros',      price:8.50,   oldPrice:null,   stock:'in',  compat:['Golf Azul','Seat León','Peugeot 308'],     isNew:false, specs:{Tipo:'Cartucho',          Altura:'82mm',       Diámetro:'72mm', Garantía:'1 año'} },
  { id:3,  emoji:'🔩',  name:'Junta de culata',              brand:'Febi',    ref:'03741',         cat:'motor',        price:34.20,  oldPrice:42.00,  stock:'low', compat:['Golf Azul'],                              isNew:false, specs:{Material:'MLS multicapa',  Espesor:'1.2mm',     Cilindros:4,     Garantía:'2 años'} },
  { id:4,  emoji:'⚡',  name:'Bujía de encendido Iridium',   brand:'NGK',     ref:'ILZKAR7A11',    cat:'electricidad', price:14.90,  oldPrice:null,   stock:'in',  compat:['Golf Azul','Peugeot 308'],                isNew:true,  specs:{Electrodo:'Iridio',       Rosca:'M14x1.25',    Apertura:'0.7mm',Garantía:'3 años'} },
  { id:5,  emoji:'💧',  name:'Bomba de agua',                brand:'Valeo',   ref:'506903',        cat:'motor',        price:62.00,  oldPrice:78.00,  stock:'in',  compat:['Seat León','Peugeot 308'],                isNew:false, specs:{Caudal:'120 l/min',       Material:'Aluminio', Diámetro:'58mm', Garantía:'2 años'} },
  { id:6,  emoji:'🔋',  name:'Alternador remanufacturado',   brand:'Valeo',   ref:'437534',        cat:'electricidad', price:145.00, oldPrice:190.00, stock:'low', compat:['Golf Azul'],                              isNew:false, specs:{Tensión:'14V',            Amperaje:'90A',      Regulador:'Interno', Garantía:'2 años'} },
  // FRENOS
  { id:7,  emoji:'🔴',  name:'Pastillas de freno delanteras',brand:'Brembo',  ref:'P50075',        cat:'frenos',       price:42.50,  oldPrice:null,   stock:'in',  compat:['Golf Azul','Seat León'],                  isNew:false, specs:{Posición:'Delantera',      Material:'Semimetálico', Espesor:'18mm', Garantía:'2 años'} },
  { id:8,  emoji:'⭕',  name:'Disco de freno ventilado',     brand:'Brembo',  ref:'09.7461.11',    cat:'frenos',       price:58.00,  oldPrice:null,   stock:'in',  compat:['Golf Azul'],                              isNew:true,  specs:{Diámetro:'280mm',         Espesor:'22mm',      Tipo:'Ventilado',Garantía:'2 años'} },
  { id:9,  emoji:'🟤',  name:'Líquido de frenos DOT 5.1',   brand:'Bosch',   ref:'1987479110',    cat:'frenos',       price:12.90,  oldPrice:null,   stock:'in',  compat:['Golf Azul','Seat León','Peugeot 308'],     isNew:false, specs:{Tipo:'DOT 5.1',           Volumen:'500ml',     'Pto. Ebullición':'270°C', Garantía:'N/A'} },
  // SUSPENSIÓN
  { id:10, emoji:'🌀',  name:'Amortiguador delantero',       brand:'Monroe',  ref:'G8085',         cat:'suspension',   price:79.00,  oldPrice:95.00,  stock:'in',  compat:['Golf Azul','Peugeot 308'],                isNew:false, specs:{Posición:'Delantero',      Tipo:'Gas',          Carrera:'150mm', Garantía:'3 años'} },
  { id:11, emoji:'🔗',  name:'Rótula de dirección',          brand:'Febi',    ref:'14044',         cat:'suspension',   price:22.40,  oldPrice:null,   stock:'in',  compat:['Seat León'],                              isNew:false, specs:{Rosca:'M14x1.5',          Cono:'1:12',         Tipo:'Rótula exterior', Garantía:'2 años'} },
  { id:12, emoji:'🟠',  name:'Silent-block de suspensión',   brand:'Monroe',  ref:'MK395',         cat:'suspension',   price:18.60,  oldPrice:null,   stock:'low', compat:['Golf Azul','Seat León'],                  isNew:false, specs:{Material:'Caucho-metal',   Diámetro:'50mm',     Altura:'45mm',   Garantía:'1 año'} },
  // FILTROS
  { id:13, emoji:'💨',  name:'Filtro de aire deportivo',     brand:'Bosch',   ref:'S0217',         cat:'filtros',      price:19.90,  oldPrice:null,   stock:'in',  compat:['Golf Azul','Seat León','Peugeot 308'],     isNew:true,  specs:{Tipo:'Panel',             Material:'Papel plisado', Tamaño:'290x145mm', Garantía:'1 año'} },
  { id:14, emoji:'🌿',  name:'Filtro habitáculo carbón activo',brand:'Bosch', ref:'1987432508',    cat:'filtros',      price:16.40,  oldPrice:22.00,  stock:'in',  compat:['Golf Azul','Peugeot 308'],                isNew:false, specs:{Tipo:'Carbón activo',      Bacterias:'99%',     Partículas:'95%',Garantía:'N/A'} },
  { id:15, emoji:'⛽',  name:'Filtro de combustible',        brand:'NGK',     ref:'KL147',         cat:'filtros',      price:24.80,  oldPrice:null,   stock:'in',  compat:['Seat León','Peugeot 308'],                isNew:false, specs:{Tipo:'Gasolina',          Presión:'6 bar',     Caudal:'90 l/h', Garantía:'1 año'} },
  // NEUMÁTICOS
  { id:16, emoji:'🔵',  name:'Neumático verano 205/55 R16',  brand:'Michelin',ref:'PRIM5',         cat:'neumaticos',   price:95.00,  oldPrice:115.00, stock:'in',  compat:['Golf Azul','Seat León'],                  isNew:false, specs:{Medida:'205/55R16',       Índice:'91V',        Temporada:'Verano',  Garantía:'5 años'} },
  { id:17, emoji:'❄️',  name:'Neumático invierno 205/55 R16',brand:'Michelin',ref:'ALPIN6',        cat:'neumaticos',   price:109.00, oldPrice:null,   stock:'low', compat:['Golf Azul','Seat León'],                  isNew:true,  specs:{Medida:'205/55R16',       Índice:'91H',        Temporada:'Invierno', Garantía:'5 años'} },
  // ELECTRICIDAD
  { id:18, emoji:'🔌',  name:'Sensor MAF caudal de aire',    brand:'Bosch',   ref:'0280218116',    cat:'electricidad', price:74.00,  oldPrice:88.00,  stock:'in',  compat:['Golf Azul'],                              isNew:false, specs:{Señal:'0–5V',             Conector:'5 pines',  Posición:'Pre-filtro', Garantía:'2 años'} },
  { id:19, emoji:'🕯️',  name:'Bobina de encendido',          brand:'Valeo',   ref:'245048',        cat:'electricidad', price:38.50,  oldPrice:null,   stock:'in',  compat:['Golf Azul','Peugeot 308'],                isNew:false, specs:{Tensión:'12V',            Pico:'40kV',         Tipo:'Lápiz',    Garantía:'2 años'} },
  // CARROCERÍA / ILUMINACIÓN
  { id:20, emoji:'🪟',  name:'Escobilla limpiaparabrisas 600mm',brand:'Valeo',ref:'574748',        cat:'carroceria',   price:14.20,  oldPrice:null,   stock:'in',  compat:['Golf Azul','Seat León','Peugeot 308'],     isNew:false, specs:{Longitud:'600mm',         Tipo:'Flat blade',   Conector:'Top lock', Garantía:'1 año'} },
  { id:21, emoji:'💡',  name:'Juego bulbos H7 55W',          brand:'Bosch',   ref:'1987302171',    cat:'iluminacion',  price:11.80,  oldPrice:null,   stock:'in',  compat:['Golf Azul','Seat León'],                  isNew:false, specs:{Tipo:'H7',               Potencia:'55W',      Tensión:'12V',   Garantía:'1 año'} },
  { id:22, emoji:'🌟',  name:'Kit LED H7 6000K',             brand:'Valeo',   ref:'032526',        cat:'iluminacion',  price:59.90,  oldPrice:75.00,  stock:'low', compat:['Golf Azul','Seat León','Peugeot 308'],     isNew:true,  specs:{Tipo:'LED H7',           Temperatura:'6000K', Lúmenes:6000,    Garantía:'3 años'} },
];

const CATEGORY_LABELS = {
  all:'Todas', motor:'Motor', frenos:'Frenos', suspension:'Suspensión',
  electricidad:'Electricidad', filtros:'Filtros', neumaticos:'Neumáticos',
  carroceria:'Carrocería', iluminacion:'Iluminación'
};

let activeFilters = {
  cat: 'all', stock: 'all', brand: 'all',
  search: '', compat: '', priceMin: '', priceMax: '', sort: 'featured'
};
let cart = [];

// ── HELPERS ──
const $ = id => document.getElementById(id);

function showToast(msg) {
  const t = $('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2600);
}

function stockInfo(s) {
  if (s === 'in')  return { dot: '',    label: 'En stock' };
  if (s === 'low') return { dot: 'low', label: 'Pocas unidades' };
  return { dot: 'out', label: 'Sin stock' };
}

// ── CART ──
function updateCartUI() {
  const count = cart.reduce((s, i) => s + i.qty, 0);
  const total = cart.reduce((s, i) => s + i.price * i.qty, 0);

  const countEl = $('cartCount');
  countEl.textContent = count;
  countEl.classList.toggle('visible', count > 0);

  const itemsEl  = $('cartItems');
  const emptyEl  = $('cartEmpty');
  const totalEl  = $('cartTotal');

  if (cart.length === 0) {
    itemsEl.innerHTML = '';
    emptyEl.style.display = 'block';
    totalEl.style.display = 'none';
  } else {
    emptyEl.style.display = 'none';
    totalEl.style.display = 'block';
    itemsEl.innerHTML = cart.map(item => `
      <div class="cart-item">
        <div class="cart-item-emoji">${item.emoji}</div>
        <div class="cart-item-info">
          <strong>${item.name}</strong>
          <span>${item.brand} · x${item.qty}</span>
        </div>
        <div class="cart-item-price">${(item.price * item.qty).toFixed(2)} €</div>
        <button class="cart-item-remove" onclick="removeFromCart(${item.id})">✕</button>
      </div>
    `).join('');
    $('cartTotalAmount').textContent = total.toFixed(2) + ' €';
  }
}

function addToCart(id) {
  const p = PRODUCTS.find(x => x.id === id);
  if (!p) return;
  const existing = cart.find(x => x.id === id);
  if (existing) existing.qty++;
  else cart.push({ ...p, qty: 1 });
  updateCartUI();
  showToast(`✓ ${p.name} añadido al carrito`);
}

function removeFromCart(id) {
  cart = cart.filter(x => x.id !== id);
  updateCartUI();
}

// ── FILTERING & SORTING ──
function getFiltered() {
  let list = [...PRODUCTS];
  if (activeFilters.cat   !== 'all') list = list.filter(p => p.cat   === activeFilters.cat);
  if (activeFilters.stock !== 'all') list = list.filter(p => p.stock === activeFilters.stock);
  if (activeFilters.brand !== 'all') list = list.filter(p => p.brand === activeFilters.brand);
  if (activeFilters.compat)          list = list.filter(p => p.compat.includes(activeFilters.compat));
  if (activeFilters.priceMin !== '')  list = list.filter(p => p.price >= parseFloat(activeFilters.priceMin));
  if (activeFilters.priceMax !== '')  list = list.filter(p => p.price <= parseFloat(activeFilters.priceMax));
  if (activeFilters.search) {
    const q = activeFilters.search.toLowerCase();
    list = list.filter(p =>
      p.name.toLowerCase().includes(q)  ||
      p.brand.toLowerCase().includes(q) ||
      p.ref.toLowerCase().includes(q)
    );
  }
  switch (activeFilters.sort) {
    case 'price-asc':  list.sort((a, b) => a.price - b.price); break;
    case 'price-desc': list.sort((a, b) => b.price - a.price); break;
    case 'name':       list.sort((a, b) => a.name.localeCompare(b.name)); break;
    case 'new':        list.sort((a, b) => b.isNew - a.isNew); break;
  }
  return list;
}

// ── RENDER PRODUCTS ──
function renderProducts() {
  const list  = getFiltered();
  const grid  = $('productsGrid');
  const empty = $('emptyState');

  $('resultsLabel').textContent = `${list.length} resultado${list.length !== 1 ? 's' : ''}`;
  $('totalCount').textContent   = PRODUCTS.length;

  if (list.length === 0) {
    grid.innerHTML = '';
    empty.style.display = 'block';
    return;
  }
  empty.style.display = 'none';

  grid.innerHTML = list.map(p => {
    const si    = stockInfo(p.stock);
    const isOut = p.stock === 'out';
    return `
      <div class="product-card" onclick="openDetail(${p.id})">
        <div class="product-img">
          ${p.emoji}
          <div class="product-badges">
            ${p.isNew    ? '<span class="badge badge-new">Nuevo</span>'   : ''}
            ${p.oldPrice ? '<span class="badge badge-offer">Oferta</span>' : ''}
          </div>
          <button class="fav-btn" onclick="event.stopPropagation(); this.classList.toggle('active')">♥</button>
        </div>
        <div class="product-body">
          <div class="product-brand">${p.brand}</div>
          <div class="product-name">${p.name}</div>
          <div class="product-ref">Ref: ${p.ref}</div>
          <div class="product-compat">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/>
            </svg>
            ${p.compat.length} vehículo${p.compat.length !== 1 ? 's' : ''} compatibles
          </div>
          <div class="product-footer">
            <div>
              <span class="product-price">
                ${p.price.toFixed(2)} €
                ${p.oldPrice ? `<span class="old-price">${p.oldPrice.toFixed(2)} €</span>` : ''}
              </span>
              <div style="display:flex;align-items:center;margin-top:0.25rem;">
                <span class="stock-dot ${si.dot}"></span>
                <span class="stock-label">${si.label}</span>
              </div>
            </div>
            <button class="add-btn" ${isOut ? 'disabled' : ''} onclick="event.stopPropagation(); addToCart(${p.id})">
              ${isOut ? 'Agotado' : '+ Añadir'}
            </button>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

// ── RENDER CATEGORY TABS ──
function renderCategoryTabs() {
  const cats = ['all','motor','frenos','suspension','filtros','electricidad','neumaticos','carroceria','iluminacion'];
  $('categoryTabs').innerHTML = cats.map(cat => {
    const count = cat === 'all' ? PRODUCTS.length : PRODUCTS.filter(p => p.cat === cat).length;
    return `
      <button class="cat-tab ${activeFilters.cat === cat ? 'active' : ''}" data-cat="${cat}">
        ${CATEGORY_LABELS[cat]} <span class="count">${count}</span>
      </button>
    `;
  }).join('');

  document.querySelectorAll('.cat-tab').forEach(btn => {
    btn.addEventListener('click', () => {
      activeFilters.cat = btn.dataset.cat;
      document.querySelectorAll('.cat-tab').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      // sync sidebar chips
      document.querySelectorAll('#catFilters .filter-chip').forEach(b =>
        b.classList.toggle('active', b.dataset.cat === activeFilters.cat)
      );
      renderProducts();
    });
  });
}

// ── DETAIL PANEL ──
function openDetail(id) {
  const p = PRODUCTS.find(x => x.id === id);
  if (!p) return;
  const si = stockInfo(p.stock);

  $('detailContent').innerHTML = `
    <div class="detail-emoji">${p.emoji}</div>
    <p class="eyebrow">${p.brand}</p>
    <h2 style="font-family:var(--font-heading);margin:0.25rem 0 0.5rem;font-size:1.75rem;">${p.name}</h2>
    <div class="detail-meta">
      ${p.isNew    ? '<span class="badge badge-new">Nuevo</span>'    : ''}
      ${p.oldPrice ? '<span class="badge badge-offer">Oferta</span>' : ''}
      <span class="badge badge-compat">${p.compat.length} compatible${p.compat.length !== 1 ? 's' : ''}</span>
    </div>
    <div style="color:var(--muted);font-size:0.85rem;margin-bottom:0.5rem;">Ref: ${p.ref}</div>
    <div class="detail-price">
      ${p.price.toFixed(2)} €
      ${p.oldPrice
        ? `<span style="font-size:1rem;color:var(--muted);text-decoration:line-through;font-family:var(--font-body);margin-left:0.5rem;">${p.oldPrice.toFixed(2)} €</span>`
        : ''}
    </div>
    <div style="display:flex;align-items:center;gap:0.4rem;margin-bottom:1rem;">
      <span class="stock-dot ${si.dot}"></span>
      <span style="color:var(--muted);font-size:0.85rem;">${si.label}</span>
    </div>
    <p class="label" style="margin-bottom:0.5rem;">Compatibilidad</p>
    <div style="display:flex;gap:0.4rem;flex-wrap:wrap;margin-bottom:0.5rem;">
      ${p.compat.map(c => `<span class="badge badge-compat">${c}</span>`).join('')}
    </div>
    <p class="label" style="margin:1rem 0 0.5rem;">Especificaciones</p>
    <div class="detail-specs">
      ${Object.entries(p.specs).map(([k, v]) =>
        `<div class="spec-item"><span>${k}</span><strong>${v}</strong></div>`
      ).join('')}
    </div>
    <div class="detail-actions">
      <button class="detail-add-btn" ${p.stock === 'out' ? 'disabled' : ''}
        onclick="addToCart(${p.id}); closeDetail()">
        ${p.stock === 'out' ? 'Sin stock' : '🛒 Añadir al carrito'}
      </button>
      <button class="detail-ghost-btn" onclick="closeDetail()">Cerrar</button>
    </div>
  `;
  $('detailOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeDetail() {
  $('detailOverlay').classList.remove('open');
  document.body.style.overflow = '';
}

// ── EVENT LISTENERS ──
$('detailClose').addEventListener('click', closeDetail);
$('detailOverlay').addEventListener('click', e => {
  if (e.target === $('detailOverlay')) closeDetail();
});

$('cartBtn').addEventListener('click', () => {
  $('cartOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
});
$('cartClose').addEventListener('click', () => {
  $('cartOverlay').classList.remove('open');
  document.body.style.overflow = '';
});
$('cartOverlay').addEventListener('click', e => {
  if (e.target === $('cartOverlay')) {
    $('cartOverlay').classList.remove('open');
    document.body.style.overflow = '';
  }
});

$('searchInput').addEventListener('input', e => {
  activeFilters.search = e.target.value;
  renderProducts();
});
$('compatSelect').addEventListener('change', e => {
  activeFilters.compat = e.target.value;
  renderProducts();
});
$('sortSelect').addEventListener('change', e => {
  activeFilters.sort = e.target.value;
  renderProducts();
});

let priceTimer;
[$('priceMin'), $('priceMax')].forEach(el => {
  el.addEventListener('input', () => {
    clearTimeout(priceTimer);
    priceTimer = setTimeout(() => {
      activeFilters.priceMin = $('priceMin').value;
      activeFilters.priceMax = $('priceMax').value;
      renderProducts();
    }, 400);
  });
});

document.querySelectorAll('#catFilters .filter-chip').forEach(btn => {
  btn.addEventListener('click', () => {
    activeFilters.cat = btn.dataset.cat;
    document.querySelectorAll('#catFilters .filter-chip').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    // sync tabs
    document.querySelectorAll('.cat-tab').forEach(b =>
      b.classList.toggle('active', b.dataset.cat === activeFilters.cat)
    );
    renderProducts();
  });
});

document.querySelectorAll('#stockFilters .filter-chip').forEach(btn => {
  btn.addEventListener('click', () => {
    activeFilters.stock = btn.dataset.stock;
    document.querySelectorAll('#stockFilters .filter-chip').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    renderProducts();
  });
});

document.querySelectorAll('#brandFilters .filter-chip').forEach(btn => {
  btn.addEventListener('click', () => {
    activeFilters.brand = btn.dataset.brand;
    document.querySelectorAll('#brandFilters .filter-chip').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    renderProducts();
  });
});

// ── INIT ──
renderCategoryTabs();
renderProducts();
updateCartUI();
