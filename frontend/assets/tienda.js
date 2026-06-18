// --- Estado ---
let activeFilters = {
    cat: 'all', stock: 'all', brand: 'all',
    search: '', compat: '', priceMin: '', priceMax: '', sort: 'featured'
};
let cart = [];
let allParts = [];

// --- Elementos DOM ---
const $ = id => document.getElementById(id);
const productsGrid = $('productsGrid');
const emptyState = $('emptyState');
const resultsLabel = $('resultsLabel');
const totalCount = $('totalCount');

// --- Funciones de API ---
async function fetchParts(filters = {}) {
    const params = new URLSearchParams();
    if (filters.cat && filters.cat !== 'all') params.append('category', filters.cat);
    if (filters.brand && filters.brand !== 'all') params.append('brand', filters.brand);
    if (filters.stock && filters.stock !== 'all') params.append('stock_status', filters.stock);
    if (filters.search) params.append('search', filters.search);
    if (filters.priceMin) params.append('min_price', filters.priceMin);
    if (filters.priceMax) params.append('max_price', filters.priceMax);
    if (filters.sort) params.append('sort', filters.sort);
    params.append('limit', '100');

    const res = await fetch(`/api/v1/parts?${params.toString()}`);
    if (!res.ok) throw new Error('Error al obtener piezas');
    return await res.json();
}

async function fetchPartDetail(id) {
    const res = await fetch(`/api/v1/parts/${id}`);
    if (!res.ok) throw new Error('Error al obtener detalle');
    return await res.json();
}

async function createOrder(items) {
    const payload = { items: items.map(i => ({ part_id: i.id, quantity: i.qty })) };
    const res = await fetch('/api/v1/orders/checkout', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });
    if (!res.ok) {
        const err = await res.json();
        throw new Error(err.detail || 'Error al crear el pedido');
    }
    return await res.json();
}

// --- Renderizado ---
function renderProducts(parts) {
    allParts = parts;
    const list = parts;
    resultsLabel.textContent = `${list.length} resultado${list.length !== 1 ? 's' : ''}`;
    totalCount.textContent = list.length;

    if (list.length === 0) {
        productsGrid.innerHTML = '';
        emptyState.style.display = 'block';
        return;
    }
    emptyState.style.display = 'none';

    productsGrid.innerHTML = list.map(p => {
        const stockLabel = p.stock > 0 ? (p.stock < 5 ? 'Pocas unidades' : 'En stock') : 'Sin stock';
        const dotClass = p.stock > 0 ? (p.stock < 5 ? 'low' : '') : 'out';
        const isNew = false; // Podríamos tener campo en la API, pero no lo tenemos
        return `
            <div class="product-card" onclick="openDetail('${p.id}')">
                <div class="product-img">
                    <span style="font-size:2.8rem;">🔧</span>
                    <div class="product-badges">
                        ${isNew ? '<span class="badge badge-new">Nuevo</span>' : ''}
                        ${p.oldPrice ? '<span class="badge badge-offer">Oferta</span>' : ''}
                    </div>
                    <button class="fav-btn" onclick="event.stopPropagation(); this.classList.toggle('active')">♥</button>
                </div>
                <div class="product-body">
                    <div class="product-brand">${p.brand}</div>
                    <div class="product-name">${p.name}</div>
                    <div class="product-ref">Ref: ${p.reference || '—'}</div>
                    <div class="product-compat">
                        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                            <circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/>
                        </svg>
                        ${p.compatibility ? p.compatibility.length : 0} vehículo${p.compatibility && p.compatibility.length !== 1 ? 's' : ''} compatibles
                    </div>
                    <div class="product-footer">
                        <div>
                            <span class="product-price">${p.price.toFixed(2)} €</span>
                            ${p.oldPrice ? `<span class="old-price">${p.oldPrice.toFixed(2)} €</span>` : ''}
                            <div style="display:flex;align-items:center;margin-top:0.25rem;">
                                <span class="stock-dot ${dotClass}"></span>
                                <span class="stock-label">${stockLabel}</span>
                            </div>
                        </div>
                        <button class="add-btn" ${p.stock <= 0 ? 'disabled' : ''} onclick="event.stopPropagation(); addToCart('${p.id}')">
                            ${p.stock <= 0 ? 'Agotado' : '+ Añadir'}
                        </button>
                    </div>
                </div>
            </div>
        `;
    }).join('');
}

// --- Filtros y recarga ---
async function applyFilters() {
    try {
        const parts = await fetchParts(activeFilters);
        renderProducts(parts);
    } catch (error) {
        console.error('Error aplicando filtros:', error);
        productsGrid.innerHTML = '<p>Error al cargar las piezas.</p>';
    }
}

// --- Carrito ---
function updateCartUI() {
    const count = cart.reduce((s, i) => s + i.qty, 0);
    const total = cart.reduce((s, i) => s + i.price * i.qty, 0);
    $('cartCount').textContent = count;
    $('cartCount').classList.toggle('visible', count > 0);

    const itemsEl = $('cartItems');
    const emptyEl = $('cartEmpty');
    const totalEl = $('cartTotal');

    if (cart.length === 0) {
        itemsEl.innerHTML = '';
        emptyEl.style.display = 'block';
        totalEl.style.display = 'none';
    } else {
        emptyEl.style.display = 'none';
        totalEl.style.display = 'block';
        itemsEl.innerHTML = cart.map(item => `
            <div class="cart-item">
                <div class="cart-item-emoji">🔧</div>
                <div class="cart-item-info">
                    <strong>${item.name}</strong>
                    <span>${item.brand} · x${item.qty}</span>
                </div>
                <div class="cart-item-price">${(item.price * item.qty).toFixed(2)} €</div>
                <button class="cart-item-remove" onclick="removeFromCart('${item.id}')">✕</button>
            </div>
        `).join('');
        $('cartTotalAmount').textContent = total.toFixed(2) + ' €';
    }
}

function addToCart(id) {
    const p = allParts.find(x => x.id === id);
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

async function checkout() {
    if (cart.length === 0) return;
    try {
        const order = await createOrder(cart);
        showToast(`✅ Pedido realizado (${order.items.length} piezas)`);
        cart = [];
        updateCartUI();
        $('cartOverlay').classList.remove('open');
        // Recargar productos para actualizar stock
        await applyFilters();
    } catch (error) {
        alert('Error al procesar el pedido: ' + error.message);
    }
}

// --- Detalle ---
async function openDetail(id) {
    try {
        const p = await fetchPartDetail(id);
        $('detailContent').innerHTML = `
            <div class="detail-emoji">🔧</div>
            <p class="eyebrow">${p.brand}</p>
            <h2 style="font-family:var(--font-heading);margin:0.25rem 0 0.5rem;font-size:1.75rem;">${p.name}</h2>
            <div class="detail-meta">
                <span class="badge badge-compat">${p.compatibility ? p.compatibility.length : 0} compatible${p.compatibility && p.compatibility.length !== 1 ? 's' : ''}</span>
            </div>
            <div style="color:var(--muted);font-size:0.85rem;margin-bottom:0.5rem;">Ref: ${p.reference || '—'}</div>
            <div class="detail-price">${p.price.toFixed(2)} €</div>
            <div style="display:flex;align-items:center;gap:0.4rem;margin-bottom:1rem;">
                <span class="stock-dot ${p.stock > 0 ? (p.stock < 5 ? 'low' : '') : 'out'}"></span>
                <span style="color:var(--muted);font-size:0.85rem;">${p.stock > 0 ? (p.stock < 5 ? 'Pocas unidades' : 'En stock') : 'Sin stock'}</span>
            </div>
            <p class="label" style="margin-bottom:0.5rem;">Compatibilidad</p>
            <div style="display:flex;gap:0.4rem;flex-wrap:wrap;margin-bottom:0.5rem;">
                ${(p.compatibility || []).map(c => `<span class="badge badge-compat">${c}</span>`).join('')}
            </div>
            <p class="label" style="margin:1rem 0 0.5rem;">Especificaciones</p>
            <div class="detail-specs">
                ${Object.entries(p.specs || {}).map(([k, v]) =>
                    `<div class="spec-item"><span>${k}</span><strong>${v}</strong></div>`
                ).join('')}
            </div>
            <div class="detail-actions">
                <button class="detail-add-btn" ${p.stock <= 0 ? 'disabled' : ''} onclick="addToCart('${p.id}'); closeDetail()">
                    ${p.stock <= 0 ? 'Sin stock' : '🛒 Añadir al carrito'}
                </button>
                <button class="detail-ghost-btn" onclick="closeDetail()">Cerrar</button>
            </div>
        `;
        $('detailOverlay').classList.add('open');
        document.body.style.overflow = 'hidden';
    } catch (error) {
        console.error('Error cargando detalle:', error);
    }
}

function closeDetail() {
    $('detailOverlay').classList.remove('open');
    document.body.style.overflow = '';
}

// --- Eventos UI ---
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

// Botón de checkout en el carrito
document.querySelector('.cart-checkout').addEventListener('click', checkout);

// Filtros de búsqueda, precio, etc.
$('searchInput').addEventListener('input', e => {
    activeFilters.search = e.target.value;
    applyFilters();
});
$('compatSelect').addEventListener('change', e => {
    activeFilters.compat = e.target.value;
    applyFilters();
});
$('sortSelect').addEventListener('change', e => {
    activeFilters.sort = e.target.value;
    applyFilters();
});

let priceTimer;
[$('priceMin'), $('priceMax')].forEach(el => {
    el.addEventListener('input', () => {
        clearTimeout(priceTimer);
        priceTimer = setTimeout(() => {
            activeFilters.priceMin = $('priceMin').value;
            activeFilters.priceMax = $('priceMax').value;
            applyFilters();
        }, 400);
    });
});

// Filtros de categoría, stock, marca (sidebar)
document.querySelectorAll('#catFilters .filter-chip').forEach(btn => {
    btn.addEventListener('click', () => {
        activeFilters.cat = btn.dataset.cat;
        document.querySelectorAll('#catFilters .filter-chip').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        // sincronizar tabs
        document.querySelectorAll('.cat-tab').forEach(b =>
            b.classList.toggle('active', b.dataset.cat === activeFilters.cat)
        );
        applyFilters();
    });
});

document.querySelectorAll('#stockFilters .filter-chip').forEach(btn => {
    btn.addEventListener('click', () => {
        activeFilters.stock = btn.dataset.stock;
        document.querySelectorAll('#stockFilters .filter-chip').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        applyFilters();
    });
});

document.querySelectorAll('#brandFilters .filter-chip').forEach(btn => {
    btn.addEventListener('click', () => {
        activeFilters.brand = btn.dataset.brand;
        document.querySelectorAll('#brandFilters .filter-chip').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        applyFilters();
    });
});

// Tabs de categorías (arriba)
document.querySelectorAll('.cat-tab').forEach(btn => {
    btn.addEventListener('click', () => {
        activeFilters.cat = btn.dataset.cat;
        document.querySelectorAll('.cat-tab').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        // sincronizar sidebar
        document.querySelectorAll('#catFilters .filter-chip').forEach(b =>
            b.classList.toggle('active', b.dataset.cat === activeFilters.cat)
        );
        applyFilters();
    });
});

// Toast
function showToast(msg) {
    const t = $('toast');
    t.textContent = msg;
    t.classList.add('show');
    setTimeout(() => t.classList.remove('show'), 2600);
}

// --- Inicialización ---
applyFilters();
updateCartUI();