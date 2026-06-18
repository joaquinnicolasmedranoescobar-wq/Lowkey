// ─── Usuarios por defecto ────────────────────────────────────────────────────
const DEFAULT_USERS = {
  jose:    { name: 'Jose Luis', password: 'admin' },
  joaquin: { name: 'Joaquin',   password: 'admin' },
  hector:  { name: 'Hector',    password: 'admin' },
};

// ─── Helpers de almacenamiento ───────────────────────────────────────────────

function getUsers() {
  const stored = localStorage.getItem('lk_users');
  return stored ? JSON.parse(stored) : { ...DEFAULT_USERS };
}

function saveUsers(users) {
  localStorage.setItem('lk_users', JSON.stringify(users));
}

// ─── LOGIN ───────────────────────────────────────────────────────────────────

const loginForm = document.getElementById('loginForm');

if (loginForm) {
  loginForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const username = document.getElementById('username').value.trim().toLowerCase();
    const password = document.getElementById('password').value.trim();
    const errorMessage = document.getElementById('errorMessage');

    const users = getUsers();

    if (users[username] && users[username].password === password) {
      localStorage.setItem('usuario', users[username].name);
      window.location.href = 'index.html';
    } else {
      errorMessage.textContent = 'Usuario o contraseña incorrectos.';
    }
  });
}

// ─── REGISTRO ────────────────────────────────────────────────────────────────

const registerForm = document.getElementById('registerForm');

if (registerForm) {
  registerForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const fullname        = document.getElementById('fullname').value.trim();
    const username        = document.getElementById('username').value.trim().toLowerCase();
    const password        = document.getElementById('password').value.trim();
    const passwordConfirm = document.getElementById('passwordConfirm').value.trim();
    const errorMessage    = document.getElementById('errorMessage');
    const successMessage  = document.getElementById('successMessage');

    // Limpiar mensajes previos
    errorMessage.textContent  = '';
    successMessage.textContent = '';

    // Validaciones
    if (!fullname || !username || !password || !passwordConfirm) {
      errorMessage.textContent = 'Por favor, rellena todos los campos.';
      return;
    }

    if (username.length < 3) {
      errorMessage.textContent = 'El usuario debe tener al menos 3 caracteres.';
      return;
    }

    if (password.length < 4) {
      errorMessage.textContent = 'La contraseña debe tener al menos 4 caracteres.';
      return;
    }

    if (password !== passwordConfirm) {
      errorMessage.textContent = 'Las contraseñas no coinciden.';
      return;
    }

    const users = getUsers();

    if (users[username]) {
      errorMessage.textContent = 'Ese nombre de usuario ya está en uso.';
      return;
    }

    // Guardar nuevo usuario
    users[username] = { name: fullname, password };
    saveUsers(users);

    // Feedback y redirigir al login
    successMessage.textContent = '¡Cuenta creada! Redirigiendo al inicio de sesión…';
    registerForm.reset();

    setTimeout(() => {
      window.location.href = 'log.html';
    }, 1800);
  });
}