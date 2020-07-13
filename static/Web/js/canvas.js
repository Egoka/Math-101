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
    canvas.onmousedown = startDrawing;
    //////////////////////
    canvas.ontouchstart = handleStart;
    //////////////////////
    document.getElementById("line").innerHTML = context.lineWidth;
}
//////////////////////////////////////////////////////////
function startup(){
	context.lineCap =['round'];
	context.lineJoin = ['bevel'];
}
///////////////////////////////////////////////////////////////////////////
function startDrawing(e) {
	isDrawing = true;// Начинаем рисовать
	context.beginPath();// Создаем новый путь (с текущим цветом и толщиной линии)
	// Нажатием левой кнопки мыши помещаем "кисть" на холст
	context.moveTo(e.pageX - canvas.offsetLeft, e.pageY - canvas.offsetTop);
}
///////////////////////////////////////////////////////////////////////////
function handleStart(e) {
     for (var i = 0; i < e.changedTouches.length; i++) {
         context.beginPath();
         context.fill();
     }
}