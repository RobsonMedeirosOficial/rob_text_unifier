// =============================================================================
// TABS DO DEMO
// =============================================================================
document.querySelectorAll('.demo-tab').forEach(tab => {
    tab.addEventListener('click', () => {
        // Remove active de todos
        document.querySelectorAll('.demo-tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.demo-panel').forEach(p => p.classList.remove('active'));
        
        // Adiciona active no clicado
        tab.classList.add('active');
        const panelId = tab.getAttribute('data-tab');
        document.getElementById(panelId).classList.add('active');
    });
});

// =============================================================================
// SMOOTH SCROLL PARA LINKS INTERNOS
// =============================================================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// =============================================================================
// ANIMAÇÃO DE SCROLL (Navbar)
// =============================================================================
let lastScroll = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
        navbar.style.background = 'rgba(15, 23, 42, 0.98)';
        navbar.style.boxShadow = '0 5px 20px rgba(0, 0, 0, 0.3)';
    } else {
        navbar.style.background = 'rgba(15, 23, 42, 0.9)';
        navbar.style.boxShadow = 'none';
    }
    
    lastScroll = currentScroll;
});

// =============================================================================
// ANIMAÇÃO DE ENTRADA DOS ELEMENTOS
// =============================================================================
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.querySelectorAll('.feature-card, .step, .demo-container').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'all 0.6s ease';
    observer.observe(el);
});

// =============================================================================
// CONSOLE EASTER EGG
// =============================================================================
console.log(`
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   🤖  rob_text_unifier                                    ║
║                                                           ║
║   Gostou do código? Contribua no GitHub!                 ║
║   https://github.com/SEU_USUARIO/rob_text_unifier        ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
`);