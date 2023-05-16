let fighter_1 = {
    FullName: 'Mike Tyson',
    Mass: 98,
    Height:193
}

let fighter_2 = {
    FullName: 'Evander Holyfield',
    Mass:96,
    Height:197
}

function BMI_func(person){
    let bmi = person.Mass/person.Height**2
    return bmi
}

function BMI_compare(person1, person2){
    bmi1 = BMI_func(person1)
    bmi2 = BMI_func(person2)
    if (bmi1 > bmi2){
        console.log(`${person1.FullName} has a larger BMI`)
    }
    else{
        console.log(`${person2.FullName} has a larger BMI`)
    }
}

BMI_compare(fighter_1,fighter_2)