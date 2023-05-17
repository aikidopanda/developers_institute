//Exercise 5
let getdiv = document.getElementsByTagName("div")
console.log(getdiv[0].innerText)
document.getElementsByTagName("li")[1].innerText = 'Richard'
let element = document.getElementsByTagName("li")[3]
element.remove()
uls = document.getElementsByTagName("ul")

for (let item of uls){
    console.log(uls[item])
    item.classList.add('student_list')
    item.firstElementChild.innerText = 'Alexey'
}

let listitems = document.getElementsByTagName("li")

for (let item of listitems){
    if (item.innerHTML == 'Richard'){
        item.style.border = "solid black 1px"
    }
}

uls[0].classList.add('university')
uls[0].classList.add('attendance')
let div = document.getElementById('container')
div.style.backgroundColor = "lightblue"
listitems[0].style.display = "None"
document.body.style.fontSize = "25px"

if (div.style.backgroundColor == "lightblue"){
    alert(`Hello ${div.innerText}`) // Not sure if I understand what is 'user in the div'properly, but let it be like this
}

