//Exercise 1
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

//Exercise 2
function find_avg(gradesList){
    let sum = gradesList.reduce(function(a, b){
        return a + b;
      })
    return sum/gradesList.length
}

grades = [90, 87, 75, 53, 46]
avg = find_avg(grades)
if (avg >= 65){
    console.log(`You have passed. Your average score is ${avg}`)
}
else{
    console.log(`Your average score is ${avg}. You have not passed`)
}