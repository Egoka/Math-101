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
    canvas.onmouseup = stopDrawing;
    canvas.onmouseout = stopDrawing;
    canvas.onmousemove = draw;
    //////////////////////
    canvas.ontouchstart = handleStart;
    canvas.ontouchend = handleEnd;
    canvas.ontouchcancel = handleCancel;
    canvas.ontouchmove = handleMove;
    //////////////////////
    document.getElementById("line").innerHTML = context.lineWidth;
}
//////////////////////////////////////////////////////////
function startup(){
	context.lineCap =['round'];
	context.lineJoin = ['bevel'];
}
//////////////////////////////////////////////////////////////////////////
function changeColor(pan_eraser){
	if (pan_eraser === true){context.globalCompositeOperation = 'destination-out';}
	else                    {context.globalCompositeOperation = 'source-over';}
}
//////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////
function startDrawing(e) {
	isDrawing = true;// Начинаем рисовать
	context.beginPath();// Создаем новый путь (с текущим цветом и толщиной линии)
	// Нажатием левой кнопки мыши помещаем "кисть" на холст
	context.moveTo(e.pageX - canvas.offsetLeft, e.pageY - canvas.offsetTop);
}
///////////////////////////////////////////////////////////////////////////
function stopDrawing() {isDrawing = false;}
///////////////////////////////////////////////////////////////////////////
function draw(e) {
	if (isDrawing === true)
	{
	  	// Определяем текущие координаты указателя мыши
		const x = e.pageX - canvas.offsetLeft;
		const y = e.pageY - canvas.offsetTop;
		// Рисуем линию до новой координаты
		context.lineTo(x, y);
		context.stroke();
	}
}
///////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////
function handleStart(e) {
     for (var i = 0; i < e.changedTouches.length; i++) {
         context.beginPath();
         context.fill();
     }
}
///////////////////////////////////////////////////////////////////////////
function handleEnd(e) {
  e.preventDefault();
  for (var i = 0; i < e.changedTouches.length; i++) {
      context.moveTo(e.changedTouches[i].pageX, e.changedTouches[i].pageY);
  }
}
function handleCancel(e) {
  e.preventDefault();
  for (var i = 0; i < e.changedTouches.length; i++) {ongoingTouches.splice(i, 1);  }
}
///////////////////////////////////////////////////////////////////////////
function handleMove(e) {
  e.preventDefault();
  for (var i = 0; i < e.changedTouches.length; i++) {
      context.lineTo(e.changedTouches[i].pageX - canvas.offsetLeft, e.changedTouches[i].pageY - canvas.offsetTop);
      context.stroke();
  }
}