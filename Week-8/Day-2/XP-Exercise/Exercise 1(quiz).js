// // Exercise 1
// // Analyse the code below, and predict what will be the value of a in all the following functions.
// // Write your prediction as comments in a js file. Explain your predictions.
// // #1
// function funcOne() {
//     let a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`); // answer: a = 3
// }

// // #1.1 - run in the console:
// funcOne()
// // #1.2 What will happen if the variable is declared 
// // with const instead of let ? 
// // answer: it will remain 5 since const cant be changed

// //#2
// let a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`); // answer: a = 0 but after the funcTwo is called it will be 5
// }

// // #2.1 - run in the console:
// funcThree()
// funcTwo()
// funcThree()
// // #2.2 What will happen if the variable is declared 
// // with const instead of let ?
// // answer: it will remain 0

// //#3
// function funcFour() {
//     window.a = "hello";
// }


// function funcFive() {
//     alert(`inside the funcFive function ${a}`); // answer: it remains 5
// }

// // #3.1 - run in the console:
// funcFour()
// funcFive()

// //#4
// let a = 1;
// function funcSix() {
//     let a = "test";
//     alert(`inside the funcSix function ${a}`);//answer: a will be 'test' because function scope in this case overrides previous 'let a = 1'
// }


// // #4.1 - run in the console:
// funcSix()
// // #4.2 What will happen if the variable is declared 
// // with const instead of let ?

// //#5
// let a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);//answer: here a will be 5
// }
// alert(`outside of the if block ${a}`);// answer: and here it will be 2

// // #5.1 - run the code in the console
// // #5.2 What will happen if the variable is declared 
// // with const instead of let ?
// //answer: it will give an error since const cant be declared both outside and inside the func

//Exercise 2

// function winBattle(){
//     return true;
// 
winBattle = () => true

let experiencePoints = winBattle == true ? 10 : 1
console.log(experiencePoints)

//Exercise 3
isString = text => typeof text == 'string' ? true : false
console.log(isString('Hello'))
console.log(isString(5))

//Exercise 4
const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
for (let i=0; i<colors.length; i++){
    console.log(`The #${i+1} color is ${colors[i]}`)
}
colorCheck = (color) => colors.includes(color) ? true : false
//testing
colorCheck('Violet') == true ? console.log('Yeah') : console.log('No...')
colorCheck('Black') == true ? console.log('Yeah') : console.log('No...')

//Exercise 5
const ordinal = ["th","st","nd","rd"];
colors.forEach((item, index) => console.log(`${index+1}${ordinal[index+1] || ordinal[0]} choice is ${item}`))

//Exercise 6
let bankAmount = 5000
const vat = 0.17
let details = [900, -300, -102, -145, -134]

for (expense of details){
    if (expense < 0){
        expense += expense * vat
    }
    // console.log(expense) // returns modified value, as intended
    // console.log(details) // returns the original array, dont know why
    bankAmount += expense
}
console.log(bankAmount)



