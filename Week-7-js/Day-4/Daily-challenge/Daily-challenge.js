planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

for (planet in planets){
    let planetdiv = document.createElement('div')
    planetdiv.setAttribute('class', 'planet')
    planetdiv.setAttribute('id', planets[planet])
    let section = document.querySelector('section')
    section.appendChild(planetdiv)
}

document.getElementById('Mercury').style.backgroundColor = 'orange'
document.getElementById('Venus').style.backgroundColor = 'blue'
document.getElementById('Earth').style.backgroundColor = 'lightblue'
document.getElementById('Mars').style.backgroundColor = 'red'
document.getElementById('Jupiter').style.backgroundColor = 'azure'
document.getElementById('Saturn').style.backgroundColor = 'gray'
document.getElementById('Uranus').style.backgroundColor = 'gold'
document.getElementById('Neptune').style.backgroundColor = 'darkblue'

// Made it without moons, for now

