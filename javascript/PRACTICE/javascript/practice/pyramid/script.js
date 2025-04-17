
// # def pyramid(n):
// #     for i in range(1,n+1):
// #         for j in range(n-i):
// #             print("  ",end="")
// #         for k in range((2*i)-1):
// #             print("*",end=" ")
// #         print()
// # pyramid(10)
//  function to print * as pyramid


function pyramid(x){
    var   row="";
    var result="";
    for (let i = 1; i <= x; i++) {
        for (let j = 1; j <= x-i; j++) {
            row+="&nbsp;";
        }
        for (let k = 1; k <=(2*i)-1; k++) {
            row+="*";
        }
        row+="\n";

    }
    result+=row
    // document.getElementById("demo").innerHTML=`<pre>${result}</pre>`;
   document.getElementById("demo").innerHTML=result;
    console.log(result)
}
pyramid(5);

    