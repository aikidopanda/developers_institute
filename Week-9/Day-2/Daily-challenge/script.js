//challenge 1
function makeAllCaps(arr){
    let notAString = false
    for (item of arr){
        if (typeof item != 'string'){
            notAString = true
        }
    }
    let myPromise = new Promise((resolve, reject) => {
        if (notAString == true){
            reject('One of the array elements is not a string!')
        }
        else{
            newArr = []
            for (item of arr){
                newArr.push(item.toUpperCase())
            }
            resolve(newArr)
        }
    })
    return myPromise
}

function sortWords(arr){
    let myPromise = new Promise((resolve, reject) => {
        if (arr.length <= 4){
            reject('The array is too short')
        }
        else{
            let sorted = arr.sort()
            resolve(sorted)
        }
    })
    return myPromise
}
//testing
makeAllCaps(['Yellow', 'Sky', 'Table', 'Cat', 'Computer']).then((arr) => sortWords(arr)).then((result) => console.log(result))
.catch(error => console.log(error))

makeAllCaps(['Yellow', 2, 'Table', 'Cat', 'Computer']).then((arr) => sortWords(arr)).then((result) => console.log(result))
.catch(error => console.log(error))

makeAllCaps(['Yellow', 'Cat', 'Computer']).then((arr) => sortWords(arr)).then((result) => console.log(result))
.catch(error => console.log(error))

//challenge 2
const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`

function toJS(json){
    let myPromise = new Promise((resolve, reject) => {
        json = json.trim()
        if (json == ''){
            reject('The json you provided is empty!')
        }
        else{
            let morseObject = JSON.parse(morse)
            resolve(morseObject)
        }
    }
    )
    return myPromise
}
//testing
// toJS('')
// .then((result) => console.log(result))
// .catch((error) => console.log(error))

toJS(morse).then((obj) => toMorse(obj)).then((arr)=>stringJoin(arr)).then((result) => console.log(result))
.catch((error) => console.log(error))
let userInput

function toMorse(obj){
    userInput = prompt('Enter a word or a sentence (lowercase)')
    let temp = userInput.split('')
    console.log(temp)
    let unexpectedSymbol = false
    let translation = []
    for (item of temp){
        if (!Object.keys(obj).includes(item)){
            unexpectedSymbol = true
        }
        else{
            let char = obj[item]
            translation.push(char)
        }
    }
    let myPromise = new Promise((resolve, reject) => {
        if (unexpectedSymbol == true){
            reject('You entered an unexpected symbol! Try again')
        }
        else{
            resolve(translation)
        }
    })
    return myPromise
}

function stringJoin(arr){
    let joined = arr.join('\n')
    let newpar = document.createElement('p')
    newpar.innerText = `The morse translation of '${userInput}' is:\n` + joined
    document.querySelector('body').appendChild(newpar)
}




