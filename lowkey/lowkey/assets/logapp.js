const loginForm = document.getElementById('loginForm');
const errorMessage = document.getElementById('errorMessage');

const users = {
  jose: 'Jose Luis',
  joaquin: 'Joaquin',
  hector: 'Hector'
};

function readStoredUsers() {
  try {
    const rawUsers = localStorage.getItem('lowkeyUsers');
    return rawUsers ? JSON.parse(rawUsers) : {};
  } catch {
    return {};
  }
}

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
  const storedUsers = readStoredUsers();

  if ((users[username] && password === 'admin') || (storedUsers[username] && storedUsers[username].password === password)) {
    // Guardar nombre del usuario
    localStorage.setItem('usuario', users[username] || storedUsers[username].fullName);

    // Redirigir al dashboard
    window.location.href = '../index.html';
  } else {
    errorMessage.textContent =
      'Usuario o contraseña incorrectos.';
  }
});