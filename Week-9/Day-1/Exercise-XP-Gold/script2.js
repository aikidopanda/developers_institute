const queryString = window.location.search;
console.log(queryString);
const urlParams = new URLSearchParams(queryString);
const firstName = urlParams.get('firstname')
const lastName = urlParams.get('lastname')
console.log(firstName, lastName)

let user = {
    'name': firstName,
    'lastname': lastName
}
let userJson = JSON.stringify(user)
console.log(userJson)
newpar = document.createElement('p')
newpar.innerText = userJson
document.querySelector('body').appendChild(newpar)