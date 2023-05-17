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
    for (let char in string){
        if (string[char] == string[char].toUpperCase()){
            string[char] = string[char].toLowerCase()
        }
        else{
            string[char] = string[char].toUpperCase()
        }
    }
    return string
}
console.log(swapper('Hello World'))
