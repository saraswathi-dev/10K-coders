let btn = document.querySelector("button");
let taskContainer = document.getElementById("taskContainer");
btn.addEventListener("click", () => {
    let inputTag = document.getElementById("task").value.trim();
    if (inputTag == "") {
        alert("Please enter task");
    }
    let taskDiv = document.createElement("div");
    taskDiv.innerHTML = `<span>${inputTag}</span>
                        <button>Edit</button>
                        <button id="delbutton">Delete</Delete>`;
    taskContainer.appendChild(taskDiv);
    let delButton = taskDiv.querySelector(".delbutton")
    delButton.addEventListener("click", () => {
        let confirmation = confirm("are you sure to delete?");
        if (confirmation) {
            taskDiv.remove();
            alert("removed successfully");  
        }
    })

    let editButton=taskDiv.querySelector(".editbutton");
    editButton.addEventListener("click",()=>{
        let newTask=prompt("Enter new task:")
        if (newTask){
            taskDiv.querySelector(".text_task").innerText=newTask.trim();
        }
    })
})

