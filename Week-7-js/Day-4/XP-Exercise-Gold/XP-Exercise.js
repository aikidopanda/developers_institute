//Exercise 1
function is_blank(string){
    if (string == ''){
        return true
    }
    else{
        return false
    }
}
teststr = ''
teststr2 = 'efeuhfwufh'
console.log(is_blank(teststr))
console.log(is_blank(teststr2))

//Exercise 2
function abbrevName(fullname){
    breakpoint = fullname.indexOf(' ')
    res = fullname.slice(0, breakpoint + 2)
    return res + '.'
}
console.log(abbrevName('Alexey Soroker'))

//Exercise 3
function swapper(string){
    let newstr = ''
    for (let char in string){
        if (string[char] == string[char].toUpperCase()){
            newstr = newstr + string[char].toLowerCase()
        }
        else{
            newstr = newstr + string[char].toUpperCase()
        }
    }
    return newstr
}
console.log(swapper('Hello World'))

//Exercise 4
function isOmnipresent(array,value){
    for (let i=0; i<array.length; i++){
        if (!array[i].includes(value)){
            return false
        }
        return true
    }
}
let myArr = [[3,4],[4,8],[4,5],[4,9]]
console.log(isOmnipresent(myArr,4))
console.log(isOmnipresent(myArr,5))
console.log(isOmnipresent(myArr,2))
