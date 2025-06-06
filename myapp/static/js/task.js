//const done = document.querySelectorAll('.done');
const status = document.querySelectorAll('.status');
const tarea = document.querySelectorAll('h2');
const task = document.querySelectorAll('.task');

const yes = task[0].childNodes[1].textContent[0];
console.log(task[0].childNodes[3].textContent) //status
console.log(task[0].childNodes[7].childNodes[3])//titulo


task.forEach(btn => {
    let done = btn.childNodes[7].childNodes[3];
    done.addEventListener('click', function(){
        //cambiar icono
        let title = btn.childNodes[1].textContent.substring(1,18);
        let icon = btn.childNodes[1].textContent[0];
        title = yes + title;
        btn.childNodes[1].textContent = title;
    })
})
