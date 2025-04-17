let alertButton=document.getElementById("alert")
let promptButton=document.getElementById("prompt")
let confirmButton=document.getElementById("confirm")
let swiggyButton=document.getElementById("swiggy")
let printButton=document.getElementById("print")



alertButton.addEventListener("click",()=>{
    window.alert("I think you are good")
})
promptButton.addEventListener("click",()=>{
    window.prompt("I think you are good if not mention how are you:")
})
confirmButton.addEventListener("click",()=>{
    window.confirm("you are good?")
})
swiggyButton.addEventListener("click",()=>{
    // window.location.href="https://www.swiggy.com/"
     window.open("https://www.swiggy.com/","_blank")  // to open in new page with out using location
})
printButton.addEventListener("click",()=>{
    window.print()
})