// for (let i = 0; i < array.length; i++) {
//             if (indexCounter == 5 || i == array.length - 1) {
//                 indexCounter = 0;
//                 final_array.push(sub_array)
//                 sub_array = [];
//             }
//             sub_array.push(array[i]);
//             indexCounter++

//         }
//         document.getElementById("demo").innerText = final_array;
//         console.log(final_array);
function a(x,y){
    x(y)
}
function b(xyz){
    xyz()
}
function c(){
    console.log("hi")
}
a(b,c)