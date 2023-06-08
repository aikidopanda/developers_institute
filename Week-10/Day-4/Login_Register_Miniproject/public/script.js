let submitLogin = document.getElementById('submit-login')
let submitRegister = document.getElementById('submit-register')

let formLogin = document.forms[0]
let formRegister = document.forms[1]

for (item of formLogin.elements){
    if (item != submitLogin){
        item.addEventListener("input", checker)
    }
}

for (item of formRegister.elements){
    if (item != submitRegister){
        item.addEventListener("input", checker1)
    }
}

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

function checker1(){
    let block = false
    for (item of formRegister.elements){
        console.log(item.value)
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