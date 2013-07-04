var niter=1;

function draw(){
	var canvas = document.getElementById("canvas");
	if (canvas.getContext) {
		var ctx = canvas.getContext("2d");
		ctx.setTransform(1,0,0,1,canvas.width/2.0,canvas.height/2.0);
		
		var linesize=10;
		niter=(niter)%6 +1;
		
		var nSteps = niter;
		
		var angle=Math.PI/5.0;
		var procedure = new Array();
		procedure.push(3,7,4,1,1,3,7,4,1,1,3,7,4,1,1,3,7,4,1,1,3,7,4);
		//procedure.push(7);
		
		//carry out the itrative procedure evolution nSteps times see Wikipedia->Penorse Tiling
		for(iti=0;iti<nSteps;++iti){
			tmpproc=new Array();
			for(element in procedure){
				switch(procedure[element]){
					case 6:
						tmpproc.push(8,5,1,1,9,5,2,2,2,2,7,5,3,2,8,5,2,2,2,2,6,5,4,1,1);
						break;
					case 7:
						tmpproc.push(1,8,5,2,2,9,5,3,2,2,2,6,5,2,2,7,5,4,1);
						break;
					case 8:
						tmpproc.push(2,6,5,1,1,7,5,3,1,1,1,8,5,1,1,9,5,4,2);
						break;
					case 9:
						tmpproc.push(2,2,8,5,1,1,1,1,6,5,3,1,9,5,1,1,1,1,7,5,4,2,2,7,5);
						break;
					case 5:
						break;
					default:
						tmpproc.push(procedure[element]);
				}
			}
			procedure = tmpproc;
			//console.log(procedure);
		}
		
		
		ctx.clearRect(-canvas.width/2.0,-canvas.height/2.0,canvas.width,canvas.height);
		
		//Now draw according to drawing rules
		for(element in procedure){
			switch(procedure[element]){
				case 5:
					//draw forward
					ctx.beginPath();
					ctx.moveTo(0,0);
					ctx.lineTo(linesize,0);
					ctx.stroke();
					ctx.translate(linesize,0);
					break;
				case 1:
					//turn left
					ctx.rotate(-angle);
					break;
				case 2:
					//turn right
					ctx.rotate(angle);
					break;
				case 3:
					ctx.save();
					break;
				case 4:
					ctx.restore();
					break;
				default:
			}
		}
	}
}
