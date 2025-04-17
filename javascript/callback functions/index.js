  function part1(item,nextStep){
           console.log(`you ordered ${item}`)
           next()
        }
        part1("Laptop Dell",function next(){
           console.log('and we will delivered soon!')
        })


        // function part1(item,nextStep){
        //     console.log(`you ordered ${item}`)
        //     setTimeout(()=>{
        //         nextStep()
        //     },3000)
            
        // }
        // part1("Laptop Dell",function next(){
        //     console.log('and we will delivered soon!')
        // })

        // function part1(item,nextStep){
        //     alert(`you ordered ${item}`)
        //     setTimeout(()=>{
        //         nextStep()
        //     },3000)
            
        // }
        // part1("Laptop Dell",()=>{
        //     alert('and we will delivered soon!')
        // })

        
        // function part1(item,nextStep){      //nested callback function
        //     setTimeout(()=>{
        //         alert(`you ordered ${item}`)
        //     },2000)
        //     setTimeout(()=>{
        //         nextStep()
        //     },3000)
        // }
        // part1("Laptop Dell",()=>{
        //     alert('and we will delivered soon!')
        // })

        // setTimeout(()=>{
        //     alert("you ordered Laptop")
        //     setTimeout(()=>{
        //         alert('we will ship soon!')
        //         setTimeout(()=>{
        //             alert('order shipped')
        //         },6000)
        //     },4000)
        // },4000)