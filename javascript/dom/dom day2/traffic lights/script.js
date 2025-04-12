const div=document.getElementById("container");
document.body.appendChild(div)
div.style.backgroundColor="blue";
div.style.height="200px";
div.style.width="200px"

function red(){
    const red=document.getElementById("red");
    const yellow=document.getElementById("yellow");
    const green=document.getElementById("green");
     yellow.style.backgroundColor="white"
      green.style.backgroundColor="white"
    red.style.backgroundColor="red";
    red.style.height="100px";
    red.style.width="100px";
    red.style.border="2px solid red"
    red.style.borderRadius="50%"
}
function yellow(){
    const red=document.getElementById("red");
    const yellow=document.getElementById("yellow");
    const green=document.getElementById("green");
     red.style.backgroundColor="white"
      green.style.backgroundColor="white"
    yellow.style.backgroundColor="yellow"
    yellow.style.height="100px";
    yellow.style.width="100px";
    yellow.style.border="2px solid yellow"
    yellow.style.borderRadius="50%"
}
function green(){
    const red=document.getElementById("red");
    const yellow=document.getElementById("yellow");
    const green=document.getElementById("green");
     yellow.style.backgroundColor="white"
      red.style.backgroundColor="white"
    green.style.backgroundColor="green"
    green.style.height="100px";
    green.style.width="100px";
    green.style.border="2px solid green"
    green.style.borderRadius="50%"
}