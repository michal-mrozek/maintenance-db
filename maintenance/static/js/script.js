const tasks = document.getElementsByClassName("task");
const twoWeeksFromToday = addWeeks(new Date(), 2);

for (let i = 0; i < tasks.length; i++) {
    const dueDate = new Date(tasks[i].children[4].innerText);
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
