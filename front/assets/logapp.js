const loginForm = document.getElementById('loginForm');
const errorMessage = document.getElementById('errorMessage');

const users = {
  jose: 'Jose Luis',
  joaquin: 'Joaquin',
  hector: 'Hector'
};

loginForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const username = document
    .getElementById('username')
    .value
    .trim()
    .toLowerCase();

  const password = document
    .getElementById('password')
    .value
    .trim();

  if (users[username] && password === 'admin') {
    // Guardar nombre del usuario
    localStorage.setItem('usuario', users[username]);

    // Redirigir al dashboard
    window.location.href = 'index.html';
  } else {
    errorMessage.textContent =
      'Usuario o contraseña incorrectos.';
  }
});