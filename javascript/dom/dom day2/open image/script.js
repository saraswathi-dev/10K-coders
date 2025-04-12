function openImage(){
    let imgTag=document.querySelector("img");
    let imgSrc=imgTag.getAttribute("src")
    // imgTag.setAttribute(width,"100")
      window.open(imgSrc,'_blank')
}

// function openImage(){
//     let imgTag=document.querySelector("img");
//     imgTag.removeAttribute("height")
// }