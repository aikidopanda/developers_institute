let timer = document.getElementById('timer')

function updateCountdown() {
  fetch('/countdown')
    .then(response => response.json())
    .then(timeRemaining => {
      if (timeRemaining.seconds > 0){
        timer.textContent = `Seconds left: ${timeRemaining.seconds}`
      }
      else{
        timer.textContent = 'Your time is up!'
      }
    }
    )
}

setInterval(updateCountdown, 1000);
