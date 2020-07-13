var canvas;
var context;
var ongoingTouches = [];
window.onload = function() {
    canvas = document.getElementById("canvas");
    context = canvas.getContext("2d");
}