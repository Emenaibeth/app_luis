// Obtén la URL actual
const currentLocation = window.location.pathname;

// Selecciona todos los enlaces del menú
const menuLinks = document.querySelectorAll('.nav-link');

// Recorre los enlaces y añade la clase 'active' al que coincide con la URL actual
menuLinks.forEach(link => {
    const linkPath = link.getAttribute('href'); // Obtiene el href del enlace

    // Compara la ruta actual con el href del enlace
    if (linkPath === currentLocation) {
        link.classList.add('active');
    }
});