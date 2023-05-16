// Exercise 1
let numbers = [123, 8409, 100053, 333333333, 7]
for (num in numbers){
    if (num % 3 == 0){
        console.log(`${numbers[num]} is divisible by three`)
    }
    else{
        console.log(`${numbers[num]} is not divisible by three`)
    }
}

//Exercise 2
/*let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
  }
let your_name = prompt('Please enter your name:')
let match = false
for (key in guestList){
    if (key == your_name){
        match = true
        console.log(`Hi! I am ${key} and I am from ${guestList[key]}`)
    }   
}
if (match == false){
    console.log('Hi! I am a guest')
}*/

//Exercise 3
let age = [20,5,12,43,98,55];
let sum = 0

for (let i = 0; i < age.length; i++){
    sum = sum + age[1]
}
console.log(sum)

max = Math.max(...age)
console.log(max)
