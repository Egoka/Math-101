jQuery(document).ready(function () {
    /* particlesJS.load(@dom-id, @path-json, @callback (optional)); */
    particlesJS.load('particles_painting', '../static/Web/Particles/My_settings/my-particles-config_painting.json', function() {
        console.log('callback - particles.js config loaded');
});
})