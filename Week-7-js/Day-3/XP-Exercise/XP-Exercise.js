// Exercise 1
const people = ["Greg", "Mary", "Devon", "James"];
people.shift();
people[2] = 'Jason';
people.push('Alexey');
console.log(people)
console.log(people.indexOf('Mary'))
people_new = people.slice(1,3)
console.log(people_new)
console.log(people.indexOf('Foo')) // returns -1 since there is no element with such value in the array
last = people.slice(-1)
console.log(last)
for (let i = 0; i < people.length; i++) {
    console.log(people[i])
    if (people[i] == 'Jason') {
        break;
    }
}
// Exercise 2
let colors = ['blue', 'green', 'orange', 'black', 'yellow']
for (let i=0; i < colors.length; i++){
    msg = `My favourite colour #${i + 1} is ${colors[i]}`
    if ( i == 0){
        msg = `My ${i + 1}st favourite colour is ${colors[i]}`
    }
    else if (i == 1){
        msg = `My ${i + 1}nd favourite colour is ${colors[i]}`
    }
    else if (i == 2){
        msg = `My ${i + 1}rd favourite colour is ${colors[i]}`
    }
    else{
        msg = `My ${i + 1}th favourite colour is ${colors[i]}`
    }
    console.log(msg)
}

//Exercise 3
/*let numinput = prompt('Enter a number: ')
while ( numinput < 10){
    numinput = prompt('Enter a number: ')
}
console.log(typeof(numinput))*/

//Exercise 4
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
console.log(building.numberOfFloors)
console.log(building.numberOfAptByFloor.firstFloor, building.numberOfAptByFloor.thirdFloor)
console.log(building.nameOfTenants[1], building.numberOfRoomsAndRent.dan[0])
if (building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1] > building.numberOfRoomsAndRent.dan[1]){
    building.numberOfRoomsAndRent.dan[1] = 1200
}
console.log(building.numberOfRoomsAndRent.dan[1])

//Exercise 5
const family = {
    dad: {
        person_name: 'James',
        age: 34 
    },
    mom: {
        person_name: 'Suzy',
        age: 32
    },
    son: {
        person_name: 'John',
        age:6
    },
    daughter: {
        person_name: 'Lise',
        age:8
    }
}
for (key in family){
    console.log(key)
}
for (key in family){
    console.log(family[key])
}

//Exercise 6
const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }
let result_string = ''
for (key in details){
    result_string = result_string + ' ' + key + ' ' + details[key]
}
console.log(result_string)

//Exercise 7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort()
let societyname = ''
for (let i=0; i < names.length; i++){
    societyname = societyname + names[i][0]
}
console.log(societyname)