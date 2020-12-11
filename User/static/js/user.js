var barra = document.querySelector(".barra");
const album = document.getElementById('album');
var caratulas = ["../static/img/caratula1.gif", "../static/img/caratula2.gif", "../static/img/caratula3.gif"];
const autor = document.getElementById('autor');
var nombAutor =["Little by Little","FLOW","FLOW"];
const tituloS = document.getElementById('tituloS');
var nombreSong =["Naruto Opening 3 | Kanashimi Wo Yasashisa Ni","Naruto Opening 4 | GO!!!","Naruto Shippuden Opening 6 | Sign"];
var audios = ["../static/musica/op3.mp3", "../static/musica/op4.mp3", "../static/musica/op6.mp3"];
var currentTime = document.querySelector(".tiempo");

// Creacion de un objeto de Audio

var audio = new Audio();
var actualSong = 0;

// carga la cancion

window.onload = playSong;

// empezar la cancion cargada y pausarla y reanudarla

function playSong() {
  album.src= caratulas[actualSong]
  autor.innerText = nombAutor[actualSong];
  tituloS.innerText = nombreSong[actualSong];
  audio.src = audios[actualSong];
  audio.play();
}

function togglePlayPause() {
  if (audio.paused) {
    audio.play();
    var play = document.querySelector(".play-pausa");
    play.innerHTML = '<i class="fa fa-pause"></i>';
  } else {
    audio.pause();
    play = document.querySelector(".play-pausa");
    play.innerHTML = '<i class="fa fa-play"></i>';
  }
}

// Barra de carga de la canción

audio.addEventListener("timeupdate", function() {
  var posicion = audio.currentTime / audio.duration;
  barra.style.width = posicion * 100 + "%";

  // conversion de tiempo de la cancion
  conversiondeTiempo(Math.round(audio.currentTime));

  // Al terminar la canion pasa a la siguiente

  if (audio.ended) {
    nextAudio();
  }
});

function conversiondeTiempo(segundos) {
  var min = Math.floor(segundos / 60);
  var seg = segundos % 60;
  // lets fix the songle digit
  min = min < 10 ? "0" + min : min;
  seg = seg < 10 ? "0" + seg : seg;
  currentTime.textContent = min + ":" + seg;

  // Tiempo total de la cancion
  totalTiempo(Math.round(audio.duration));
}

function totalTiempo(segundos) {
  var min = Math.floor(segundos / 60);
  var seg = segundos % 60;

  // digitos de la duración de la cancion

  min = min < 10 ? "0" + min : min;
  seg = seg < 10 ? "0" + seg : seg;
  currentTime.textContent += " & " + min + ":" + seg;
}

// Cancion siguiente y Canción anterior

function nextAudio() {
  actualSong++;
  if (actualSong > 2) {
    actualSong = 0;
  }
  playSong();
  play = document.querySelector(".play-pausa");
  play.innerHTML = '<i class="fa fa-pause"></i>';
  
}

function prevAudio() {
  actualSong--;
  if (actualSong < 0) {
    actualSong = 2;
  }
  playSong();
  play = document.querySelector(".play-pausa");
  play.innerHTML = '<i class="fa fa-pause"></i>';
}

// Bajar y Subir Volumen hasta Minimo(Mute)/Maximo

function menosVolumen() {
  audio.volume -= 0.10;
}

function masVolumen() {
  audio.volume += 0.10;
}

// Mutear/Desmutear audio/cancion

var volumenOn = document.querySelector(".volumenOn");
volumenOn.addEventListener("click", function() {
  if (audio.volume === 1) {
    audio.volume = 0;
    document.querySelector(".volumenOn i").className = "fa fa-volume-mute";
  } else {
    audio.volume = 1;
    document.querySelector(".volumenOn i").className = "fa fa-volume-up";
  }
});

var mod = document.getElementById('Modificar').style.display = 'none';
var vista = document.getElementById('CuentaU').style.display = 'none';


function ModificarUser() {
    var mod = document.getElementById("Modificar");
    if (mod.style.display === "none") {
        mod.style.display = "block";
    } else {
        mod.style.display = "none";
    }
}

function VerCuenta() {
    var vista = document.getElementById("CuentaU");
    if (vista.style.display === "none") {
        vista.style.display = "block";
    } else {
        vista.style.display = "none";
    }
}