let libform = document.getElementById('libform')
let storyfinal = document.getElementById('story')
let libbutton = libform.elements[5]

let story = [];

console.log(story)

function createStory(event){
    for (let i=0; i<5; i++){
        story[i] = libform.elements[i].value
    }
    for (item of story){
        item = item.replaceAll(' ',''); item = item.trim()
        if (item.length > 0){
            par = document.createElement('p')
            par.innerText = item
            storyfinal.appendChild(par)
            console.log(item.length)
        }
        else{
            alert('You didnt filled one of inputs')
            location.reload()
        }
    }
    event.preventDefault()
}

libbutton.addEventListener('click', createStory)



