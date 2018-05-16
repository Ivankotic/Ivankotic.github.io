var canv = document.getElementById('canvas');
var ctx = canv.getContext('2d');
var isMousedown = false;
canv.width = window.innerWidth;
canv.height = window.innerHeight;

//code
canv.addEventListener('mousedown', function(e) {
	isMousedown = true;
});
canv.addEventListener('mouseup', function(e) {
	isMousedown = false;
	ctx.beginPath();
});

ctx.lineWidth = 20;
canv.addEventListener('mousemove', function(e) {
	if (isMousedown == true) {
		ctx.lineTo(e.clientX, e.clientY);
		ctx.stroke();
		
		ctx.beginPath();
		ctx.arc(e.clientX, e.clientY, 10, 0, Math.PI * 2);
		ctx.fill();
		
		ctx.beginPath();
		ctx.moveTo(e.clientX, e.clientY);
	}
});