//Exercise 1
// 1. result == ['bread, 'carrot', 'potato, 'chicken, 'apple', 'orange]
// 2. country == ['U','S','A'] cause string is cloned into array
// 3. the output will be an array of two undefined elements, because there are two commas in original array

//Exercise 2
const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
             { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
             { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
             { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
             { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
             { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
             { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}];
let usersMapped = users.map(user => 'Welcome ' + user.firstName)
console.log(usersMapped)
let usersFiltered = users.filter(user => user.role == 'Full Stack Resident')
console.log(usersFiltered)
usersFilteredAndMapped = usersFiltered.map(user => user.lastName)
console.log(usersFilteredAndMapped)

//Exercise 3
const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];
let result = epic.reduce((a,b) => a + ' ' + b)
console.log(result)

//Exercise 4
const students = [{name: "Ray", course: "Computer Science", isPassed: true}, 
               {name: "Liam", course: "Computer Science", isPassed: false}, 
               {name: "Jenner", course: "Information Technology", isPassed: true}, 
               {name: "Marco", course: "Robotics", isPassed: true}, 
               {name: "Kimberly", course: "Artificial Intelligence", isPassed: false}, 
               {name: "Jamie", course: "Big Data", isPassed: false}];

let passed = students.filter(student => student.isPassed == true)
console.log(passed)
passed.forEach(student => console.log(`Congratulations ${student.name}, you passed the course in ${student.course}`))



