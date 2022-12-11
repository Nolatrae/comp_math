

var sec = 0;
var min = 0;
var t;
var  sw;

function initSW(){
  sw = document.getElementsByClassName('stopwatch')[0];
}
function time(){
    sec++;
    if (sec >= 60) {
        sec = 0;
        min++;
    }
}
function add() {
    time();
    sw.textContent = (min > 9 ? min : "0" + min)
       		 + ":" + (sec > 9 ? sec : "0" + sec);
    timer();
}
function timer() {
    t = setTimeout(add, 1000);
}

function off_timer(){
  clearTimeout(t);
}

function on_timer(){
  off_timer();
  sec = 0;
  min = 0;
  sw.textContent = "00:00";
}

document.addEventListener("DOMContentLoaded", initSW);