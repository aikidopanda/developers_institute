function helloWorld(){
    alert('Hello World!')
    let par = document.createElement('p')
    par.innerText = 'Hello World!'
    container.appendChild(par)
}
let interval
let container = document.getElementById('container')
function myTimer(){
    let interval = setTimeout(helloWorld, 2000)
}
// Part III
let clear = document.getElementById('clear')
function myTimer2(){
    interval = setInterval(helloWorld, 2000)
}
myTimer2()
clear.addEventListener('click', function() { clearInterval(interval) })