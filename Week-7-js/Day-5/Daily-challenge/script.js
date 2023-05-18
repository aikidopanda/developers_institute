let bottles = 99
let step = 1

while (bottles > 0){
    console.log(`${bottles} bottles of beer on the wall`)
    console.log(`${bottles} bottles of beer`)
    if (step == 1){
        console.log(`Take ${step} down, pass it around`)
    }
    else if (step >= bottles){
        console.log('Take them all down, pass them around')
    }
    else{
        console.log(`Take ${step} down, pass them around`)
    }
    bottles = bottles - step
    step++
    if (bottles <= 0){
        console.log('No bottles of beer on the wall')
    }
    else{
        console.log(`${bottles} bottles of beer on the wall`)
    }
    console.log('')
}