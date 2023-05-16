let sentence = 'The food was not bad, it was rather tasty'
// let sentence = 'The food was not that bad, it was rather tasty' // for testing purposes

// let WordNot, WordBad = sentence.indexOf('not'), sentence.indexOf('bad')

let WordNot = sentence.indexOf('not')
let WordBad = sentence.indexOf('bad')
console.log(WordNot)
console.log(WordBad)
if ( WordBad == WordNot + 4){ // seems straighforward but 4 is the exact number of characters of the word 'not' and space
    let new_sentence = sentence.replace('not bad', 'good')
    console.log(new_sentence)
}
else{
    console.log(sentence)
}
