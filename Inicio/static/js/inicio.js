var bg = ["static/img/fondo1.jpg","static/img/fondo2.jpg","static/img/fondo3.jpg","static/img/fondo4.jpg","static/img/fondo5.jpg","static/img/fondo6.jpg"]

function fondosRandom() {
var imgs = bg[Math.floor(Math.random()*bg.length)]
document.body.style.backgroundImage="url("+imgs+")";

}

function PlayStop(){
	if(videos.paused){
		$("#play").css({'background':'url(static/img/pausa1.png)'});
		videos.play();
	}else{
		videos.pause();
		$("#play").css({'background':'url(static/img/boton1.png)'});
	};

};

function silence(){
	if(videos.muted){
		$("#mute").css({'background':'url(static/img/mute1.png)'});
		videos.muted = false;
	}else{
		videos.muted = true;
		$("#mute").css({'background':'url(static/img/mute2.png)'});
	};

};

function adelanretro(value){
		videos.currentTime += value;
};


