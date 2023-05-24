//Exercise 1
function printFullName(objUser){
    let{first: firstname, last: lastname} = objUser;
    return `Your full name is ${firstname} ${lastname}`
}
console.log(printFullName({first: 'Elie', last:'Schoppik'}));

//Exercise 2
function sorter(obj){
    key_sorted = Object.keys(obj).sort()
    val_sorted = Object.values(obj).sort()
    return [key_sorted, val_sorted]
}
result = sorter({fruits: 'Banana', vegetables: 'Tomato', meat: 'Chicken', other: 'Milk'})
result1 = sorter({'James': 23, 'Victor': 19, 'Michael': 28})
console.log(result)
console.log(result1)

//Exercise 3
// output will be 3 cause classes in such aspects behave like objects
