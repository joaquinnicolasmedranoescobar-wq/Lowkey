const screenButtons = document.querySelectorAll('[data-screen]');
const screens = document.querySelectorAll('.screen');
const stepButtons = document.querySelectorAll('.step-btn');
const statusLabel = document.getElementById('statusLabel');
const previewName = document.getElementById('previewName');
const previewPlate = document.getElementById('previewPlate');
const vehicleForm = document.getElementById('vehicleForm');
const maintenanceForm = document.getElementById('maintenanceForm');

const screenMessages = {
  inicio: 'Listo para registrar tu primer coche',
  coches: 'Alta de vehículo en progreso',
  mantenimientos: 'Nuevo mantenimiento preparado',
  gastos: 'Control de costes activo',
  estadisticas: 'Resumen general disponible'
};

function showScreen(screenId) {
  screens.forEach((screen) => {
    screen.classList.toggle('active', screen.id === screenId);
  });

  stepButtons.forEach((button) => {
    button.classList.toggle('active', button.dataset.screen === screenId);
  });

  statusLabel.textContent = screenMessages[screenId] || screenMessages.inicio;
}

screenButtons.forEach((button) => {
  button.addEventListener('click', () => {
    showScreen(button.dataset.screen);
  });
});

vehicleForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const formData = new FormData(vehicleForm);
  const vehicleName = formData.get('vehicleName') || 'Nuevo vehículo';
  const plate = formData.get('plate') || 'Sin matrícula';

  previewName.textContent = vehicleName;
  previewPlate.textContent = plate;
  showScreen('mantenimientos');
});

maintenanceForm.addEventListener('submit', (event) => {
  event.preventDefault();
  showScreen('gastos');
});

showScreen('inicio');