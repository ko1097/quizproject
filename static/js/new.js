window.onload = initall;
var saveAnsButton;
function initall(){
  saveAnsButton = document.querySelector('#save_ans')
  saveAnsButton.onclick = saveans
}
function saveans() {
  var ans = $("input:radio[name=name]:checked").val()

  var req = new  XMLHttpRequest()

  var url ='/saveans?ans-'+ans

  req.open("GET",url,true)
  req.send()
}
window.onload = initall;
var saveAnsButton;
function initall(){
  saveAnsButton = document.querySelector('#save_as')
  saveAnsButton.onclick = saveas
}
function saveans() {
  var ans = $("input:radio[name=name]:checked").val()

  var req = new  XMLHttpRequest()

  var url ='/saveans?ans-'+ans

  req.open("GET",url,true)
  req.send()
}

document.querySelector('.sub').addEventListener('click',function(){
  alert("Answer have submitted Click next for next question" ) ;
});
document.querySelector('.next').addEventListener('click',function(){
  alert(document.querySelector('.para').textContent ) ;
});
var timer = document.querySelector('.last');


var myVar = setInterval(myTimer, 1000);

function myTimer() {
  const now = new Date();
  const hour = `${now.getHours()}`.padStart(2,0);
  const min = `${now.getMinutes()}`.padStart(2,0);
  const sec = `${now.getSeconds()}`.padStart(2,0);
  timer.textContent = `${hour}:${min}:${sec}`;
}
var time = document.querySelector('.lasto');


// var myVar = setInterval(myTimerMain, 1000);
//
// function myTimerMain() {
//   const now = new Date();
//   const hour = `${now.getHours()}`.padStart(2,0);
//   const min = `${now.getMinutes()}`.padStart(2,0);
//   const sec = `${now.getSeconds()}`.padStart(2,0);
//   time.textContent = `${hour}:${min}:${sec}`;
// }
