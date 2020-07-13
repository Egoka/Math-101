var canvas;
var context;
var ongoingTouches = [];
window.onload = function() {
    canvas = document.getElementById("canvas");
    context = canvas.getContext("2d");
        if(window.innerWidth>=1000)
    {
     width = window.innerWidth*0.8;
     height = window.innerHeight*0.62;
    }
    else{
    width = window.innerWidth;
    height = window.innerHeight*0.52;
    }
    canvas.width = width;
    canvas.height = height;
    context.lineWidth = 15;
    startup()
    //////////////////////
    document.getElementById("line").innerHTML = context.lineWidth;
}
//////////////////////////////////////////////////////////
function startup(){
	context.lineCap =['round'];
	context.lineJoin = ['bevel'];
}