let myForm = document.forms[0]
let fields = myForm.elements

submitButton = document.getElementById('submit')

submitButton.addEventListener('click', submit)

function submit(event){
    if ( fields[0].value.length > 0 && fields[1].value.length > 0){
        let user = {
            'name': fields[0].value,
            'lastname': fields[1].value
        }
        let userJson = JSON.stringify(user)
        let newpar = document.createElement('p')
        newpar.innerText = userJson
        document.querySelector('body').appendChild(newpar)
    }
    event.preventDefault()
}


