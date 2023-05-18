const computer_number = Math.round(Math.random() * 10) // global since its used inside the function

function playTheGame(){
    let userconfirm = confirm('Would you like to play the GuessNumber game?')
    if (userconfirm == false){
        alert('No problem. Goodbye!')
    }
    else{
        let user_number = prompt('Enter a number between 1 and 10')
        while (true){
            if (isNaN(user_number) || user_number == ''){
                alert('Please enter a valid number!')
                user_number = prompt('Enter a number between 1 and 10')
            }
            else if (user_number < 0 || user_number > 10){
                alert('Your number is out of range. Enter a number between 0 and 10')
                user_number = prompt('Enter a number between 1 and 10')
            }
            else{
                break;
            }
        }
        CompareNumbers(user_number, computer_number)
    }
}

function CompareNumbers(num1,num2){
    let attempts = 1
    while (attempts <= 3){
        if (num1 == num2){
            alert ('You guessed the secret number!')
            break;
        }
        else if (num1 > num2){
            num1 = prompt(`Your number is bigger that the secret number, try again (you made ${attempts} of 3 attempts)`)
            attempts++
        }
        else if(num1 < num2){
            num1 = prompt(`Your number is smaller that the secret number, try again (you made ${attempts} of 3 attempts)`)
            attempts++
        }
    }
    if (attempts > 3){
        alert ('You spent all of your attempts!:(')
    }
}
