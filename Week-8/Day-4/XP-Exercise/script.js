//Exercise 1
// This output will take the needed values from the object 'person'

//Exercise 2
function displayStudentInfo(objUser){
    let{first: firstname, last: lastname} = objUser;
    return `${firstname} ${lastname}`
}

console.log(displayStudentInfo({first: 'Elie', last:'Schoppik'}));

//Exercise 3
const users = { user1: 18273, user2: 92833, user3: 90315 }
let usersArray = Object.values(users)
console.log(usersArray)

usersNew = Object.values(users).map((val) => val * 2) // I don't understand how to multiply the values of the original object with such methods, so I created a new one

for (item of Object.values(users)){
    item * 2
}
console.log(users) // doesn't work as well, returns original values:(

console.log(usersNew)

//Exercise 4
// it will be an object cause its a class instance

//Exercise 5
//The second one/ It takes the namr from super-class and initiates a new attribute 'size'

//Exercise 6
// [2] === [2] false because of referencing
// {} === {} had no idea but the checking gave me a syntax error. If we initalize two empty objects and try to === them it will be also false due to referencing

// object2.number and object3.number will be 4, object4.number will remain 5 since object1 isnt copied in this case and object4 references to difference place in memory

class Animal{
    constructor(type, animalname, color){
        this.type = type
        this.animalname = animalname
        this.color = color
    }
}


class Mammal extends Animal{
    constructor(type, animalname, color, voice){
        super(type, animalname, color)
        this.voice = voice
    }
    sound(){
        console.log(`${this.animalname} the ${this.type} says '${this.voice}'`)
    }
}

farmerCow = new Mammal('cow', 'Burenka', 'brown', 'MMMOOOO')
farmerCow.sound()