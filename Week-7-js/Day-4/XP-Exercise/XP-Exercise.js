//Exercise 1
function isDivisible(){
    let sum = 0
    for (let i = 0; i <= 500; i++){
        if (i % 23 == 0){ 
            console.log(i)
            sum = sum + i
        }
    }
    console.log(`Sum: ${sum}`)
}

//Bonus
function isDivisible(divisor){
    let sum = 0
    for (let i = 0; i <= 500; i++){
        if (i % divisor == 0){ 
            console.log(i)
            sum = sum + i
        }
    }
    console.log(`Sum: ${sum}`)
}


//isDivisible()
isDivisible(56)

//Exercise 2
const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}

shoppingList = ['banana','orange','apple']

function myBill(){
    let totalprice = 0
    for (item in shoppingList){
        if (stock[shoppingList[item]] > 0){
            totalprice = totalprice + prices[shoppingList[item]];
            stock[shoppingList[item]] = stock[shoppingList[item]] - 1
        }            
    }
    return totalprice
}
console.log(myBill())

//Exercise 3
function changeEnough(itemPrice, amountOfChange){
    let sumOfChange = amountOfChange[0] * 0.25 + amountOfChange[1] * 0.1 + amountOfChange[2] * 0.05 + amountOfChange[2] * 0.01
    if (sumOfChange >= itemPrice){
        return true
    }
    else{
        return false
    }
}
console.log(changeEnough(5,[15,13,24,12]))

//Exercise 4
// function hotelcost(){
//     let userInput = prompt('How many nights would you like to stay in the hotel?')
//     if (isNaN(userInput) || userInput == ''){
//         return hotelcost()
//     }
//     else{
//         let totalprice = userInput * 140
//         return totalprice
//     }
// }
// let totalprice = hotelcost()
// console.log(`The total cost will be ${totalprice} $`)




    



