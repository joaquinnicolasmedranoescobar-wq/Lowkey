const registerForm = document.getElementById('registerForm');
const errorMessage = document.getElementById('errorMessage');

const defaultUsers = {
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

function saveStoredUsers(users) {
  localStorage.setItem('lowkeyUsers', JSON.stringify(users));
}

registerForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const fullName = document.getElementById('fullName').value.trim();
  const username = document.getElementById('username').value.trim().toLowerCase();
  const password = document.getElementById('password').value.trim();
  const confirmPassword = document.getElementById('confirmPassword').value.trim();
  const storedUsers = readStoredUsers();

  if (!fullName || !username || !password || !confirmPassword) {
    errorMessage.textContent = 'Completa todos los campos.';
    return;
  }

  if (password !== confirmPassword) {
    errorMessage.textContent = 'Las contraseñas no coinciden.';
    return;
  }

  if (defaultUsers[username] || storedUsers[username]) {
    errorMessage.textContent = 'Ese usuario ya existe.';
    return;
  }

  storedUsers[username] = { fullName, password };
  saveStoredUsers(storedUsers);

  localStorage.setItem('usuario', fullName);
  window.location.href = 'login.html';
});