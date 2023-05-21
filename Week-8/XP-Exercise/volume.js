const pi = 3.14 // approximately
let radius = document.getElementById('radius')
let volume = document.getElementById('volume')
let submit = document.getElementById('submit')

function sphereVolume(event){
    let vol = (4/3) * pi * radius.value**3
    volume.value = vol
    console.log(vol)
    event.preventDefault()
}

submit.addEventListener('click', sphereVolume)