// const axios = require('axios')

let submitRegister = document.getElementById('submit-register')
let formRegister = document.forms[0]

formRegister.addEventListener('submit', register)

for (item of formRegister.elements){
    if (item != submitRegister){
        item.addEventListener("input", checker)
    }
}

function checker(){
    let block = false
    for (item of formRegister.elements){
        if (item.value.length == 0){
            block = true
        }
    }

    if (block == true){
        submitRegister.disabled = true
    }
    else{
        submitRegister.disabled = false
    }
}

function register(event){
    event.preventDefault()
    fetch('/fetch')
    .then(response=>response.json())
    .then((data)=>{
        let dataTemp = data
        console.log(dataTemp)
        if (huy == true){
            let newpar = document.createElement('p')
            newpar.innerHTML = '<p>Your account has been created!</p>'
            document.querySelector('body').appendChild(newpar)
        }
        else{
            let newpar = document.createElement('p')
            newpar.innerHTML = '<p>This username is already in use!</p>'
            document.querySelector('body').appendChild(newpar)
        }
    })
}