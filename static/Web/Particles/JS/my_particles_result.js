jQuery(document).ready(function () {
    /* particlesJS.load(@dom-id, @path-json, @callback (optional)); */
    particlesJS.load('particles_result', '../static/Web/Particles/My_settings/my-particles-config_result.json', function() {
        console.log('callback - particles.js config loaded');
});
})