// --- Estado global ---
let currentVehicleId = localStorage.getItem('currentVehicleId') || null;

// --- Elementos DOM ---
const screens = document.querySelectorAll('.screen');
const stepButtons = document.querySelectorAll('.step-btn');
const statusLabel = document.getElementById('statusLabel');
const previewName = document.getElementById('previewName');
const previewPlate = document.getElementById('previewPlate');

// --- Funciones de navegación ---
function showScreen(screenId) {
    screens.forEach(s => s.classList.toggle('active', s.id === screenId));
    stepButtons.forEach(btn => btn.classList.toggle('active', btn.dataset.screen === screenId));
    statusLabel.textContent = {
        inicio: 'Listo para gestionar tus vehículos',
        coches: 'Registra un nuevo vehículo',
        mantenimientos: 'Gestiona los mantenimientos',
        gastos: 'Controla tus gastos',
        estadisticas: 'Resumen y estadísticas'
    }[screenId] || '';

    // Cargar datos según la pantalla
    if (screenId === 'inicio') loadDashboard();
    if (screenId === 'mantenimientos') loadMaintenances();
    if (screenId === 'gastos') loadExpenses();
    if (screenId === 'estadisticas') loadStatistics();
}

// --- Funciones de carga de datos desde la API ---

// Dashboard
async function loadDashboard() {
    try {
        const [summaryRes, statsRes] = await Promise.all([
            fetch('/api/v1/dashboard/summary'),
            fetch('/api/v1/dashboard/statistics')
        ]);
        const summary = await summaryRes.json();
        const stats = await statsRes.json();

        // Actualizar las estadísticas en la pantalla de inicio
        document.querySelector('.hero-panel .stat-pill:nth-child(1) strong').textContent = summary.total_vehicles || 0;
        document.querySelector('.hero-panel .stat-pill:nth-child(2) strong').textContent = (summary.total_expenses || 0).toFixed(2) + ' €';
        document.querySelector('.hero-panel .stat-pill:nth-child(3) strong').textContent = summary.pending_maintenances || 0;

        // También podemos actualizar la tarjeta de estado del sidebar
        // ...
    } catch (error) {
        console.error('Error cargando dashboard:', error);
    }
}

// Mantenimientos del vehículo actual
async function loadMaintenances() {
    if (!currentVehicleId) {
        document.querySelector('#mantenimientos .timeline-panel').innerHTML = '<p>No hay vehículo seleccionado. Registra uno primero.</p>';
        return;
    }
    try {
        const [listRes, alertRes] = await Promise.all([
            fetch(`/api/v1/maintenances/${currentVehicleId}`),
            fetch(`/api/v1/maintenances/${currentVehicleId}/upcoming-alert`)
        ]);
        const list = await listRes.json();
        const alert = await alertRes.json();

        // Actualizar el timeline
        const timeline = document.querySelector('#mantenimientos .timeline');
        timeline.innerHTML = list.slice(0, 3).map(m => `
            <article>
                <strong>${m.type}</strong>
                <p>${m.km} km · ${m.cost} €</p>
            </article>
        `).join('') || '<p>No hay mantenimientos registrados.</p>';

        // Actualizar alerta
        const alertBox = document.querySelector('#mantenimientos .alert-box');
        alertBox.innerHTML = `
            <strong>Próximo aviso</strong>
            <p>${alert.next_task || 'Sin alertas'} — en ${alert.due_in_days || '?'} días (${alert.due_in_km || '?'} km)</p>
        `;
    } catch (error) {
        console.error('Error cargando mantenimientos:', error);
    }
}

// Gastos del vehículo actual
async function loadExpenses() {
    if (!currentVehicleId) {
        document.querySelector('#gastos .expense-main').innerHTML = '<p>No hay vehículo seleccionado.</p>';
        return;
    }
    try {
        const [listRes, summaryRes] = await Promise.all([
            fetch(`/api/v1/expenses/${currentVehicleId}`),
            fetch(`/api/v1/expenses/${currentVehicleId}/monthly-summary`)
        ]);
        const list = await listRes.json();
        const summary = await summaryRes.json();

        // Actualizar resumen mensual
        document.querySelector('#gastos .budget-header h4').textContent =
            `${summary.total_used || 0} € usados de ${summary.budget_limit || 0} €`;
        document.querySelector('#gastos .progress-fill').style.width = `${Math.min(summary.usage_percentage || 0, 100)}%`;
        document.querySelector('#gastos .badge.warning').textContent =
            `${Math.round(summary.usage_percentage || 0)}% consumido`;

        // Categorías
        const cardsContainer = document.querySelector('#gastos .expense-cards');
        cardsContainer.innerHTML = (summary.categories || []).map(cat => `
            <div class="expense-card">
                <span>${cat.category}</span>
                <strong>${cat.amount.toFixed(2)} €</strong>
            </div>
        `).join('') || '<p>Sin gastos este mes.</p>';
    } catch (error) {
        console.error('Error cargando gastos:', error);
    }
}

// Estadísticas globales
async function loadStatistics() {
    try {
        const res = await fetch('/api/v1/dashboard/statistics');
        const stats = await res.json();

        document.querySelector('#estadisticas .stat-card:nth-child(1) strong').textContent =
            (stats.average_cost_per_vehicle || 0).toFixed(2) + ' €';
        document.querySelector('#estadisticas .stat-card:nth-child(2) strong').textContent =
            stats.quarterly_maintenance_count || 0;

        // Tendencia de gastos
        const trendList = document.querySelector('#estadisticas .trend-list');
        trendList.innerHTML = (stats.expense_trend || []).map(item => `
            <div><span>${item.category}</span><strong>${item.variation_percentage > 0 ? '+' : ''}${item.variation_percentage}%</strong></div>
        `).join('') || '<p>No hay datos de tendencia.</p>';
    } catch (error) {
        console.error('Error cargando estadísticas:', error);
    }
}

// --- Eventos de navegación ---
document.querySelectorAll('[data-screen]').forEach(btn => {
    btn.addEventListener('click', () => {
        showScreen(btn.dataset.screen);
    });
});

// --- Formulario de vehículo ---
document.getElementById('vehicleForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = {
        name: formData.get('vehicleName'),
        plate: formData.get('plate'),
        brand: formData.get('brand'),
        model: formData.get('model'),
        mileage: parseInt(formData.get('mileage')),
        fuel_type: formData.get('fuelType'),
        notes: formData.get('notes') || ''
    };
    try {
        const res = await fetch('/api/v1/vehicles', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const vehicle = await res.json();
        currentVehicleId = vehicle.id;
        localStorage.setItem('currentVehicleId', currentVehicleId);

        // Actualizar vista previa
        previewName.textContent = vehicle.name;
        previewPlate.textContent = vehicle.plate;

        showScreen('mantenimientos');
    } catch (error) {
        console.error('Error creando vehículo:', error);
        alert('Error al guardar el vehículo');
    }
});

// --- Formulario de mantenimiento ---
document.getElementById('maintenanceForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    if (!currentVehicleId) {
        alert('Primero debes registrar un vehículo.');
        return;
    }
    const formData = new FormData(e.target);
    const data = {
        vehicle_id: currentVehicleId,
        type: formData.get('type'),
        date: formData.get('date'),
        km: parseInt(formData.get('km')),
        cost: parseFloat(formData.get('cost')),
        description: formData.get('description') || ''
    };
    try {
        const res = await fetch('/api/v1/maintenances', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        if (res.ok) {
            showScreen('gastos');
        } else {
            throw new Error('Error al guardar mantenimiento');
        }
    } catch (error) {
        console.error(error);
        alert('Error al guardar el mantenimiento');
    }
});

// --- Inicialización ---
showScreen('inicio');