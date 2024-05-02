const tasks = document.getElementsByClassName("task");
const twoWeeksFromToday = addWeeks(new Date(), 1);
// const rows = tasks.children;

for (let i = 0; i < tasks.length; i++) {
    console.log(tasks[i]);
    
    console.log(twoWeeksFromToday);
    const dueDate = new Date(tasks[i].children[4].innerText);
    console.log(dueDate);
    if(new Date() > dueDate) {
    
        tasks[i].classList.add("overdue");
    }
    if(twoWeeksFromToday>dueDate) {
    
    tasks[i].classList.add("less-than-2weeks");
}
}

function addWeeks(date, weeks) {
    date.setDate(date.getDate() + 7 * weeks);
    return date;
  }
