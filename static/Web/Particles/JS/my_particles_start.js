jQuery(document).ready(function () {
    /* particlesJS.load(@dom-id, @path-json, @callback (optional)); */
    particlesJS.load('particles_start', '../static/Web/Particles/My_settings/my-particles-config_start.json', function() {
        console.log('callback - particles.js config loaded');
});
})