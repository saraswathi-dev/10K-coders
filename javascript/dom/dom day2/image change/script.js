// function imgHandler(){
//     let imgTag=document.querySelector("img");
//    imgTag.setAttribute("src","https://images.unsplash.com/photo-1575936123452-b67c3203c357?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D")
//     imgTag.setAttribute("height","100")


// }


function imgHandler() {
    let imgTag = document.querySelector("img");
    let originalSrc=imgTag.getAttribute("src")
    

    // if(originalSrc){
    //      imgTag.src = "https://images.unsplash.com/photo-1575936123452-b67c3203c357?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D"

    // }else{
    //     imgTag.src=originalSrc
    // }
    originalSrc?imgTag.src = "https://images.unsplash.com/photo-1575936123452-b67c3203c357?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D": imgTag.src;



}


// // toggle src
// function imgHandler() {
//     let imgTag = document.querySelector("img");

//     if (!imgTag.dataset.original) {
//         imgTag.dataset.original = imgTag.src;
//     }
//     imgTag.src === imgTag.dataset.original? "https://images.unsplash.com/photo-1575936123452-b67c3203c357?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D" : imgTag.dataset.original;


//     //    imgTag.src="https://images.unsplash.com/photo-1575936123452-b67c3203c357?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D"
//     //     imgTag.height="100"


// }