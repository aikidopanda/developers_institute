//Exercise 1
let sum = (a,b) => a+b
console.log(sum(4,3))

//Exercise 2
// I dont understand how to invoke func declaration and expression separately so I wrote only the final function
weightGrams = (weight) => weight*1000
myWeight = weightGrams(58.5)
console.log(myWeight)

//Exercise 3
function fortuneTeller(children, partner, location, job){
    par = document.createElement('p')
    par.innerText = `You will be a ${job} in ${location}, and married to ${partner} with ${children} kids`
    document.getElementsByTagName('body')[0].appendChild(par) 
}
(function(children, partner, location, job){
    let par = document.createElement('p')
    par.innerText = `You will be a ${job} in ${location}, and married to ${partner} with ${children} kids`
    document.getElementsByTagName('body')[0].appendChild(par) 
})(2,'Mary','USA','programmer') 

//Exercise 4 (see ex-4.js)
//Exercise 5
//Part 1
let juice_size = ['small', 'medium', 'large']
// function makeJuice(size){
//     let user_ingredients = []
//     if (juice_size.includes(size)){
//         (function(ingredients){
//             let par = document.createElement('p')
//             par.innerText = `The client wants a ${size} juice, containing ${ingredients}`
//             document.querySelector('body').appendChild(par)
//         })(user_ingredients)
//     }
//     else{
//         alert('Choose small, medium or large juice size!')
//     }
// }
// Part 2
function makeJuice(size){
    let user_ingredients = []
    if (juice_size.includes(size)){
        (function addIngredients(ing1, ing2, ing3){
            user_ingredients.push(ing1, ing2, ing3)
        })('apple', 'lemon', 'orange');
        (function addIngredients(ing1, ing2, ing3){
            user_ingredients.push(ing1, ing2, ing3)
        })('grapefruit', 'peach', 'pineapple');

        (function displayJuice(ingredients){
            let client_string = `The client wants a ${size} juice, containing `
            ingredients.forEach(item => {client_string = client_string + item + ', '})
            arrtemp = client_string.split('')
            for (let i=0; i<arrtemp.length; i++){
                if (i == arrtemp.length-2){
                    arrtemp[i] = '.'
                }
            }
            let new_string = arrtemp.join('')
            console.log(new_string)
            let par = document.createElement('p')
            par.innerText = new_string
            document.querySelector('body').appendChild(par)
        })(user_ingredients)
    }
    else{
        alert('Choose small, medium or large juice size!')
    }
}
makeJuice('small')
