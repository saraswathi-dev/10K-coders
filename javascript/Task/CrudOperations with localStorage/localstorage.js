let btn = document.querySelector("button");
let inputTag = document.getElementById("task");
let taskContainer = document.getElementById("taskContainer");
window.addEventListener("DOMContentLoaded", () => {
    const allTasks = JSON.parse(localStorage.getItem("allTasks")) || [];
    allTasks.forEach(task => createTask(task));
});

btn.addEventListener("click", () => {
    let inputTagText = inputTag.value.trim();
    if (inputTagText === "") {
        alert("Please enter task");
        return;
    }
    createTask(inputTagText);
    let allTasks = JSON.parse(localStorage.getItem("allTasks")) || [];
    allTasks.push(inputTagText)
    localStorage.setItem("allTasks", JSON.stringify(allTasks));
    inputTag.value = "";
});
function createTask(task) {
    let taskDiv = document.createElement("div");
    taskDiv.innerHTML = `<span class="text_task">${task}</span>
                <button class="editbutton">Edit</button>
                <button class="delbutton">Delete</button>`;
    taskContainer.appendChild(taskDiv);
    removeTask(taskDiv, task);
    editTask(taskDiv, task);
}
function removeTask(taskDiv, task) {
    const removeTask = taskDiv.querySelector(".delbutton")
    removeTask.addEventListener("click", () => {
        let confirmation = confirm("are you sure to delete?");
        if (confirmation) {
            taskDiv.remove();
            let allTasks = JSON.parse(localStorage.getItem("allTasks"));
            let updatedTasks = allTasks.filter(item => item != task);
            localStorage.setItem("allTasks", JSON.stringify(updatedTasks))
            alert("removed successfully");
        }
    })
}
function editTask(taskDiv, task) {
    const editTask = taskDiv.querySelector(".editbutton")
    editTask.addEventListener("click", () => {
        let confirmation = confirm("are you sure to edit?");
        if (confirmation) {
            let newTask = prompt("Enter new Task:");
            if (newTask=="") {
               alert("please enter task:");
               return;
            }
            if(newTask.trim()!==""){
                taskDiv.querySelector(".text_task").innerText = newTask.trim();
            }
            let allTasks = JSON.parse(localStorage.getItem("allTasks"));
            let updatedTasks = allTasks.map(item => item===task?newTask.trim():item);
            localStorage.setItem("allTasks", JSON.stringify(updatedTasks))
            alert("task Updated successfully");
        }
    })

}
