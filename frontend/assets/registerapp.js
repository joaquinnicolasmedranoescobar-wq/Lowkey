const registerForm = document.getElementById('registerForm');
const errorMessage = document.getElementById('errorMessage');

registerForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const fullName = document.getElementById('fullName').value.trim();
    const username = document.getElementById('username').value.trim().toLowerCase();
    const password = document.getElementById('password').value.trim();
    const confirmPassword = document.getElementById('confirmPassword').value.trim();

    if (!fullName || !username || !password || !confirmPassword) {
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
    if (password !== confirmPassword) {
        errorMessage.textContent = 'Las contraseñas no coinciden.';
        return;
    }

    const storedUsers = JSON.parse(localStorage.getItem('lowkeyUsers') || '{}');
    if (storedUsers[username]) {
        errorMessage.textContent = 'Ese nombre de usuario ya está en uso.';
        return;
    }

    storedUsers[username] = { fullName, password };
    localStorage.setItem('lowkeyUsers', JSON.stringify(storedUsers));

    errorMessage.textContent = '';
    alert('Cuenta creada correctamente. Ahora inicia sesión.');
    window.location.href = '/auth/login.html';
});