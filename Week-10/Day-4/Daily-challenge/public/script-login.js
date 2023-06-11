import axios from 'axios'

let submitLogin = document.getElementById('submit-login')
let formLogin = document.forms[0]

for (item of formLogin.elements){
    if (item != submitLogin){
        item.addEventListener("input", checker)
    }
}

formLogin.addEventListener('submit', register)

function checker(){
    let block = false
    for (item of formLogin.elements){
        console.log(item.value)
        if (item.value.length == 0){
            block = true
        }
    }

    if (block == true){
        submitLogin.disabled = true
    }
    else{
        submitLogin.disabled = false
    }
}