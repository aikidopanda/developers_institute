const fs = require('fs')
let position = 0
let sum = 0
let checked = false

fs.readFile('RightLeft.txt', 'utf-8', (err, data) => {
    for (item of data){
        sum++
        if (item == '>'){
            position++
        }
        else if (item == '<'){
            position--
        }
        if ( position == -1 && checked == false){
            console.log(`Current position is ${position}. It took ${sum} steps to reach this`)
            checked = true
        }
    }



    console.log(`Final position in the end: ${position} to the right`)
})

