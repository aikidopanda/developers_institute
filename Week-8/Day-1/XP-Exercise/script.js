//Exercise 1

let h1 = document.getElementsByTagName('h1')[0]
console.log(h1.innerText)

let p_last = document.querySelector('article').lastElementChild
p_last.style.display = 'none'

let h2 = document.querySelector('h2')
h2.addEventListener('click', function () { h2.style.backgroundColor = 'red' })

let h3 = document.querySelector('h3')
h3.addEventListener('click', function () { h3.style.display= 'none' })

let p_array = document.querySelectorAll('p')
function paragraphBold(){
    for (item of p_array){
        item.style.fontWeight = 'bold'
    }
}
let button = document.querySelector('button');
button.addEventListener('click', paragraphBold);


//h1.addEventListener('mouseover', function() { random_size = Math.round(Math.random() * 100); h1.style.fontSize = `${random_size}px`})
function fading(){
    p_array[1].classList.toggle('fade')
}
p_array[1].addEventListener('mouseover', fading)

//Exercise 3
var allBoldItems
let par = document.getElementById('exercise-3')
window.onload = getBoldItems()
function getBoldItems(){
    allBoldItems = par.getElementsByTagName('strong')
}
function highlight(){
    for (item of allBoldItems){
        item.style.color = 'blue'
    }
}
function returnNormal(){
    for (item of allBoldItems){
        item.style.color = 'black'
    }
}
par.addEventListener('mouseover', highlight)
par.addEventListener('mouseout', returnNormal)

//Exercise 5
h2.addEventListener('mouseover', function() {h2.style.color = 'yellow'})
h2.addEventListener('mouseout', function() {h2.style.fontStyle = 'italic'})