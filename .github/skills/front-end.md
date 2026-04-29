---
name: frontend-landing
description: >
  Build high-converting, production-quality landing pages and web UIs inspired by modern SaaS and eCommerce brands. Use this skill whenever the user asks to create or improve a landing page, hero section, registration form, lead gen page, product page, pricing section, signup flow, or any frontend component for a website or web app — even if they don't say "landing page" explicitly. Trigger for requests like "build me a homepage", "create a signup form", "design a hero section", "make a product showcase", "build a SaaS website", or "create a page like [well-known brand]". Always use this skill for any frontend UI task involving conversion-focused design.
---

# Frontend Landing Page Skill
## High-Converting · Retention-Focused · Modern Interactive

Build beautiful, conversion-optimized landing pages and web components following proven patterns from top SaaS, eCommerce, and B2B brands — enhanced with modern interaction and retention techniques.

---

## Core Design Principles

Extracted from reference brands (HelloFresh, Polestar, Auth0, Skillshare, Zavvy, Wix, Linear, Vercel, Loom, Notion):

### 1. Visual Hierarchy
- **Hero-first**: Every page opens with a bold, full-width or split-screen hero
- **One primary CTA**: A single dominant action button per section (never compete)
- **Typography contrast**: Large headline (3–5rem) + small supporting copy (1rem–1.1rem)
- **Whitespace is content**: Generous padding makes elements breathe and feel premium

### 2. Color Systems
| Pattern | Usage | Example Brand |
|---|---|---|
| **Dark hero + color CTA** | Premium/tech products | Polestar, Linear |
| **White card on photo background** | Consumer / food / lifestyle | HelloFresh |
| **Brand color full-bleed** | SaaS / B2B | Zavvy (purple), Skillshare (dark teal) |
| **Clean white + purple/blue accent** | Developer tools / identity | Auth0, Vercel |
| **Glassmorphism on gradient** | Modern SaaS / AI tools | Loom, Notion AI |

Always define a CSS custom property system:
```css
:root {
  --color-primary: /* main brand color */;
  --color-primary-hover: /* darkened 10% */;
  --color-bg: /* page background */;
  --color-surface: /* card/panel background */;
  --color-text: /* body text */;
  --color-text-muted: /* secondary text */;
  --color-cta: /* CTA button */;
  --radius-sm: 6px;
  --radius-md: 12px;
  --radius-lg: 20px;
  --glass-bg: rgba(255,255,255,0.08);
  --glass-border: rgba(255,255,255,0.12);
  --shadow-glow: 0 0 40px rgba(var(--primary-rgb), 0.3);
}
```

### 3. Layout Patterns

#### Split Layout (most common)
```
[Text/Form Left] | [Visual/Product Right]
```

#### Full-Width Hero with Scroll-Reveal
```
[Centered text overlay on full-bleed image/video] → content fades in on scroll
```

#### Bento Grid (trending 2024–2025)
```
[Feature cards in asymmetric grid layout] ← used by Linear, Vercel, Arc
```

#### Sticky Scroll Storytelling
```
[Fixed visual panel] + [scrollable text steps] ← used by Stripe, Apple
```

---

## Modern Technology Stack

### CDN Libraries (zero-install, embed directly)

#### 🎞️ GSAP — Professional-grade animations
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
```
```javascript
gsap.registerPlugin(ScrollTrigger);

// Staggered hero entrance
gsap.from('.hero-element', {
  opacity: 0, y: 60, duration: 0.8,
  stagger: 0.15, ease: 'power3.out'
});

// Scroll-driven counter animation
gsap.to('.stat-number', {
  textContent: '10000',
  duration: 2,
  snap: { textContent: 1 },
  scrollTrigger: { trigger: '.stats', start: 'top 80%' }
});

// Parallax section
gsap.to('.hero-bg', {
  yPercent: -30,
  ease: 'none',
  scrollTrigger: { trigger: '.hero', scrub: true }
});
```

#### 🌊 Lenis — Ultra-smooth scroll
```html
<script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>
```
```javascript
const lenis = new Lenis({ lerp: 0.08, smooth: true });
function raf(time) { lenis.raf(time); requestAnimationFrame(raf); }
requestAnimationFrame(raf);
// Connect to GSAP ScrollTrigger
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((time) => lenis.raf(time * 1000));
```

#### ✨ Three.js — 3D backgrounds & WebGL effects
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
```
```javascript
// Animated particle background
const scene = new THREE.Scene();
const geometry = new THREE.BufferGeometry();
const particles = new Float32Array(3000).map(() => (Math.random() - 0.5) * 10);
geometry.setAttribute('position', new THREE.BufferAttribute(particles, 3));
const mesh = new THREE.Points(geometry, new THREE.PointsMaterial({
  size: 0.015, color: 0x6366f1, transparent: true, opacity: 0.6
}));
scene.add(mesh);
```

#### 🎭 Motion One — Lightweight CSS animation library
```html
<script src="https://cdn.jsdelivr.net/npm/motion@10.16.4/dist/motion.js"></script>
```
```javascript
// Intersection Observer–driven entrance
const { animate, inView } = Motion;
inView('.card', ({ target }) => {
  animate(target, { opacity: [0, 1], y: [40, 0] }, { duration: 0.6, easing: [0.25, 0.1, 0.25, 1] });
});
```

#### 📊 CountUp.js — Animated statistics
```html
<script src="https://cdn.jsdelivr.net/npm/countup.js@2.8.0/dist/countUp.umd.js"></script>
```
```javascript
new countUp.CountUp('stat-users', 128000, { suffix: '+', duration: 2.5 }).start();
```

#### 🎨 Typed.js — Typewriter effect for headlines
```html
<script src="https://cdn.jsdelivr.net/npm/typed.js@2.1.0/dist/typed.umd.js"></script>
```
```javascript
new Typed('#hero-typed', {
  strings: ['10x faster.', 'beautifully simple.', 'built for teams.'],
  typeSpeed: 60, backSpeed: 30, loop: true, smartBackspace: true
});
```

#### 🌐 Vanilla Tilt — 3D card hover effect
```html
<script src="https://cdn.jsdelivr.net/npm/vanilla-tilt@1.8.1/dist/vanilla-tilt.min.js"></script>
```
```javascript
VanillaTilt.init(document.querySelectorAll('.feature-card'), {
  max: 8, speed: 400, glare: true, 'max-glare': 0.2
});
```

---

## Retention & Interaction Patterns

### 🔁 Scroll-Driven Storytelling
Pin a section and animate content as user scrolls through steps — used by Stripe, Apple, Linear:
```javascript
gsap.utils.toArray('.story-step').forEach((step, i) => {
  ScrollTrigger.create({
    trigger: step,
    start: 'top center',
    end: 'bottom center',
    toggleClass: { targets: '.story-visual', className: `active-step-${i}` }
  });
});
```

### 🏆 Progress Gamification
Keep users engaged with visible progress:
```html
<div class="progress-bar" role="progressbar" aria-valuenow="60">
  <div class="progress-fill" style="width: 60%"></div>
  <span class="progress-label">Step 2 of 3 — Almost there!</span>
</div>
```
```css
.progress-fill {
  background: linear-gradient(90deg, var(--color-primary), var(--color-cta));
  height: 4px;
  transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}
```

### 🎯 Exit-Intent Overlay
Capture users before they leave:
```javascript
document.addEventListener('mouseleave', (e) => {
  if (e.clientY <= 0 && !sessionStorage.getItem('exit-shown')) {
    gsap.to('#exit-modal', { opacity: 1, scale: 1, duration: 0.4, ease: 'back.out' });
    sessionStorage.setItem('exit-shown', 'true');
  }
});
```

### 🔔 Social Proof Toasts (FOMO)
Real-time purchase/signup notifications build trust:
```javascript
const events = [
  { name: 'María G.', city: 'Madrid', action: 'started a free trial', time: '2m ago' },
  { name: 'Carlos R.', city: 'Barcelona', action: 'upgraded to Pro', time: '5m ago' }
];
function showToast(event) {
  const toast = document.createElement('div');
  toast.className = 'fomo-toast';
  toast.innerHTML = `<img src="avatar.png"><div><strong>${event.name}</strong> from ${event.city}<br><small>${event.action} · ${event.time}</small></div>`;
  document.body.appendChild(toast);
  gsap.from(toast, { x: -100, opacity: 0, duration: 0.5 });
  setTimeout(() => gsap.to(toast, { opacity: 0, onComplete: () => toast.remove() }), 4000);
}
```

### ⏱️ Urgency Timer
Countdown timers for limited offers:
```javascript
function startCountdown(endTime, elementId) {
  const update = () => {
    const diff = endTime - Date.now();
    const h = Math.floor(diff / 3600000);
    const m = Math.floor((diff % 3600000) / 60000);
    const s = Math.floor((diff % 60000) / 1000);
    document.getElementById(elementId).textContent =
      `${String(h).padStart(2,'0')}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
  };
  setInterval(update, 1000); update();
}
```

### 🎠 Auto-scrolling Testimonial Carousel
Infinite scroll ticker (no dots, no buttons — frictionless):
```css
.ticker-wrap { overflow: hidden; }
.ticker {
  display: flex; gap: 2rem;
  animation: ticker-scroll 30s linear infinite;
}
@keyframes ticker-scroll {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}
.ticker:hover { animation-play-state: paused; }
```

### 🖱️ Custom Cursor with Magnetic Buttons
```javascript
const cursor = document.querySelector('.custom-cursor');
document.addEventListener('mousemove', ({ clientX: x, clientY: y }) => {
  gsap.to(cursor, { x, y, duration: 0.15, ease: 'power2.out' });
});
document.querySelectorAll('.btn-magnetic').forEach(btn => {
  btn.addEventListener('mousemove', (e) => {
    const rect = btn.getBoundingClientRect();
    const dx = (e.clientX - rect.left - rect.width / 2) * 0.3;
    const dy = (e.clientY - rect.top - rect.height / 2) * 0.3;
    gsap.to(btn, { x: dx, y: dy, duration: 0.3, ease: 'power2.out' });
  });
  btn.addEventListener('mouseleave', () =>
    gsap.to(btn, { x: 0, y: 0, duration: 0.5, ease: 'elastic.out(1, 0.3)' })
  );
});
```

### 🌈 Interactive Gradient Mesh Background
Modern AI-product aesthetic:
```css
.mesh-bg {
  background: radial-gradient(ellipse at 20% 50%, #7c3aed33 0%, transparent 50%),
              radial-gradient(ellipse at 80% 20%, #0ea5e933 0%, transparent 50%),
              radial-gradient(ellipse at 60% 80%, #10b98133 0%, transparent 50%),
              #0a0a0a;
  animation: mesh-shift 8s ease infinite alternate;
}
@keyframes mesh-shift {
  0%   { background-position: 0% 50%; }
  100% { background-position: 100% 50%; }
}
```

### 🪄 Glassmorphism Cards
```css
.glass-card {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-radius: var(--radius-lg);
  box-shadow: 0 8px 32px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.1);
}
```

### 💡 Bento Grid Layout (trending)
```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: auto;
  gap: 1rem;
}
.bento-card:nth-child(1) { grid-column: span 2; grid-row: span 2; }
.bento-card:nth-child(4) { grid-column: span 2; }

@media (max-width: 768px) {
  .bento-grid { grid-template-columns: 1fr; }
  .bento-card { grid-column: span 1 !important; grid-row: span 1 !important; }
}
```

---

## Modern CSS Features (2024–2025)

### Scroll-Driven Animations (native CSS, no JS)
```css
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(40px); }
  to   { opacity: 1; transform: translateY(0); }
}
.animate-on-scroll {
  animation: fade-in-up linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 40%;
}
```

### Container Queries
```css
.card-container { container-type: inline-size; }
@container (min-width: 400px) {
  .card { display: grid; grid-template-columns: 1fr 2fr; }
}
```

### :has() Selector (parent targeting)
```css
/* Highlight form when it has an error */
.form-group:has(.error-msg:not(:empty)) input {
  border-color: #ef4444;
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.2);
}
/* Show clear button only when input has content */
.input-wrapper:has(input:not(:placeholder-shown)) .clear-btn {
  display: flex;
}
```

### @layer for style organization
```css
@layer reset, base, components, utilities, overrides;
@layer components {
  .btn-primary { /* styles */ }
  .card { /* styles */ }
}
```

---

## Form Design (Conversion-Critical)

```html
<!-- Multi-step form with progress -->
<form class="multi-step-form" novalidate>
  <div class="form-progress">
    <div class="step active" data-step="1">Email</div>
    <div class="step" data-step="2">Details</div>
    <div class="step" data-step="3">Done</div>
  </div>

  <!-- Step 1 -->
  <div class="form-step active" id="step-1">
    <h3>Start for free</h3>
    <div class="input-group">
      <input type="email" id="email" placeholder=" " required>
      <label for="email">Work email</label>
      <span class="input-icon">✉</span>
    </div>
    <button type="button" class="btn-primary btn-magnetic" onclick="nextStep()">
      Continue <span class="btn-arrow">→</span>
    </button>
    <p class="trust-copy">🔒 No credit card required · Cancel anytime</p>
  </div>
</form>
```

```css
/* Floating label pattern */
.input-group { position: relative; }
.input-group input { padding: 20px 16px 8px; border: 1.5px solid #e5e7eb; border-radius: 8px; }
.input-group label {
  position: absolute; top: 50%; left: 16px;
  transform: translateY(-50%);
  transition: all 0.2s; pointer-events: none; color: #9ca3af;
}
.input-group input:focus + label,
.input-group input:not(:placeholder-shown) + label {
  top: 10px; font-size: 0.72rem; color: var(--color-primary);
}
.input-group input:focus { border-color: var(--color-primary); box-shadow: 0 0 0 3px rgba(99,102,241,0.15); }
```

---

## Navigation Patterns

```css
/* Glassmorphism sticky nav */
nav.sticky-glass {
  position: sticky; top: 0; z-index: 100;
  backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
  background: rgba(255,255,255,0.8);
  border-bottom: 1px solid rgba(0,0,0,0.06);
  transition: background 0.3s, box-shadow 0.3s;
}
nav.scrolled {
  background: rgba(255,255,255,0.95);
  box-shadow: 0 1px 20px rgba(0,0,0,0.08);
}
```
```javascript
window.addEventListener('scroll', () => {
  document.querySelector('nav').classList.toggle('scrolled', window.scrollY > 50);
});
```

---

## CTA Button System

```css
.btn-primary {
  position: relative; overflow: hidden;
  background: var(--color-cta);
  color: white; padding: 14px 28px;
  border-radius: var(--radius-sm);
  font-weight: 600; border: none; cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}
/* Shimmer effect on hover */
.btn-primary::after {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(105deg, transparent 40%, rgba(255,255,255,0.3) 50%, transparent 60%);
  transform: translateX(-100%);
  transition: transform 0.5s;
}
.btn-primary:hover { transform: translateY(-2px); box-shadow: var(--shadow-glow); }
.btn-primary:hover::after { transform: translateX(100%); }

/* Loading state */
.btn-primary.loading {
  pointer-events: none;
  background: #9ca3af;
}
.btn-primary.loading::before {
  content: '';
  display: inline-block; width: 16px; height: 16px;
  border: 2px solid white; border-top-color: transparent;
  border-radius: 50%; margin-right: 8px;
  animation: spin 0.7s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
```

---

## Page Type Playbooks

### Consumer Product Landing (e.g. HelloFresh)
1. Sticky nav: logo left, offer badge center, CTA button right
2. Hero: white card left (headline + form + price) | product photo right
3. Animated entry with GSAP stagger on load
4. Social proof: live counter ("12,847 people joined this week")
5. Scroll-triggered feature cards with Bento layout

### Premium AI / SaaS (e.g. Vercel, Linear, Loom)
1. Dark mesh-gradient background
2. Bold headline with Typed.js rotating value props
3. Glassmorphism feature cards in Bento grid
4. Interactive product demo/screenshot with hover zoom
5. FOMO toasts + animated stats on scroll
6. Pricing toggle (monthly / annual) with smooth transition

### Consumer SaaS Registration (e.g. Skillshare, Notion)
1. Split screen: value prop left | form right
2. Multi-step form with progress bar
3. Social logins (Google, GitHub, Apple)
4. Trust badges and testimonials below form
5. Exit-intent modal if user tries to leave

### eCommerce Hero (e.g. Wix, Shopify)
1. Full-bleed video or 3D product background (Three.js)
2. Urgency countdown timer ("Offer ends in 02:14:33")
3. Magnetic CTA button
4. Scrolling testimonial ticker
5. Sticky "Add to cart" bar appears after hero exits viewport

### B2B Lead Gen (e.g. Auth0, HubSpot)
1. Minimal nav, clean white background
2. Gated content form with progressive disclosure
3. Company logo strip (social proof)
4. Interactive ROI calculator
5. Auto-scroll to confirmation section on submit

---

## Performance & Accessibility

### Lazy Loading
```javascript
// Intersection Observer for images
const imgObserver = new IntersectionObserver((entries) => {
  entries.forEach(({ isIntersecting, target }) => {
    if (isIntersecting) {
      target.src = target.dataset.src;
      imgObserver.unobserve(target);
    }
  });
}, { rootMargin: '200px' });
document.querySelectorAll('img[data-src]').forEach(img => imgObserver.observe(img));
```

### Reduced Motion Respect
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
  .ticker { animation: none; }
}
```

### Core Web Vitals
- Load fonts with `font-display: swap`
- Use `will-change: transform` only on actively animating elements, remove after
- Prefer CSS animations over JS for simple transitions
- Defer non-critical scripts: `<script defer src="...">`
- Use `loading="lazy"` on below-fold images

---

## Font System (2024–2025 picks)

Avoid overused fonts (Inter, Roboto). Choose distinctive pairings:

| Mood | Headline | Body |
|---|---|---|
| Modern SaaS | `Bricolage Grotesque` | `DM Sans` |
| Premium / Luxury | `Cormorant Garamond` | `Jost` |
| Techy / Dev | `Space Grotesk` | `IBM Plex Sans` |
| Editorial | `Playfair Display` | `Lora` |
| Playful | `Fraunces` | `Nunito` |

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@400;600;700;800&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
```

---

## Output Format

1. **Single HTML file** with embedded CSS, JS, and all CDN imports
2. External CDNs allowed: Google Fonts, GSAP (cdnjs), Lenis (jsdelivr), CountUp, Typed.js, Motion One, Vanilla Tilt
3. Three.js for 3D backgrounds only when visually justified
4. Deliver via `file_create` → `/mnt/user-data/outputs/landing.html`
5. Call `present_files` to deliver to user

For React: single `.jsx`, use Tailwind + Framer Motion when available.

---

## Quick Decision Tree

```
What does the user want?
├── Full landing page
│   ├── Consumer product → HelloFresh playbook + ticker + FOMO toasts
│   ├── AI / SaaS → dark mesh bg + bento grid + Typed.js hero
│   ├── eCommerce → video hero + urgency timer + sticky cart bar
│   └── B2B lead gen → clean form + ROI calculator + logo strip
├── Hero section only → hero component + GSAP entrance + magnetic CTA
├── Signup/registration → multi-step form + social logins + progress bar
├── Lead gen / gated content → progressive form + exit-intent modal
└── "Like [brand]" → match brand above, extract palette, add retention layer
```

Always ask before coding:
1. What is the **ONE action** this page wants the user to take?
2. What **color system and mood** fits the brand?
3. Which **retention mechanisms** are appropriate (timer, FOMO, progress, gamification)?
4. Consumer (warm, photo-heavy, animated) or B2B (clean, data-driven, form-heavy)?
5. Does the complexity justify Three.js or is CSS mesh sufficient?