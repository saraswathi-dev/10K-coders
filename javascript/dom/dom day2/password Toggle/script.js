function passwordToggler(){
    let inputTage=document.getElementById("password");
    let iconTag=document.getElementById("icon");
    if(inputTage.type==="password"){
        inputTage.type="text";
        iconTag.innerText="🙈";

    }else{
        inputTage.type="password";
        iconTag.innerText="👁️";
    }
}