//Exercise 2
let form = document.querySelector('form')
console.log(form)

let firstname = document.getElementById('fname')
let lastname = document.getElementById('lname')
let submit = document.getElementById('submit')
console.log(firstname, lastname, submit)

// firstname = document.getElementsByName('fname')
// lastname = document.getElementsByName('lname')
// console.log(firstname, lastname)

let ul = document.querySelector('ul')

submit.addEventListener('click', addUserInfo)

function addUserInfo(event){
    if (firstname.value.length > 0 && lastname.value.length > 0){

        let li_fname = document.createElement('li')
        let li_fname_txt = document.createTextNode(firstname.value)
        li_fname.append(li_fname_txt)
        ul.appendChild(li_fname)
        firstname.value=''

        let li_lname = document.createElement('li')
        let li_lname_txt = document.createTextNode(lastname.value)
        li_lname.append(li_lname_txt)
        ul.appendChild(li_lname)
        lastname.value=''
    }
    event.preventDefault()
}



