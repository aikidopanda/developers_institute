function anagramCheck(word1,word2){
    let splitted1 = word1.split('')
    let splitted2 = word2.split('')
    splitted1 = splitted1.filter(char => char != ' ' && isNaN(char) == true)
    splitted2 = splitted2.filter(char => char != ' ' && isNaN(char) == true)
    let lowcase1 = []
    let lowcase2 = []
    for (char of splitted1){
        lowcase1.push(char.toLowerCase())
    }
    for (char of splitted2){
        lowcase2.push(char.toLowerCase())
    }
    if (lowcase1.length != lowcase2.length){
        alert('The strings have different length! Try again')
    }
    else{
        let processed1 = lowcase1.sort().join('')
        let processed2 = lowcase2.sort().join('')
        if ( processed1 === processed2){
            return true
        }
        return false
    }
}

//testing
console.log(anagramCheck('god','dog'))
console.log(anagramCheck('God','Ged'))
console.log(anagramCheck('God','dog'))
console.log(anagramCheck('god', 'd og'))
console.log(anagramCheck('God193', 'dog'))
console.log(anagramCheck('Godd', 'dog'))