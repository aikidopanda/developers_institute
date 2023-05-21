let container = document.getElementById('container')
let animate = document.getElementById('animate')
let pos = 0
function myMove(){
    myInterval = setInterval(moveDiv, 1)
}
function moveDiv(){
    if (pos >= 350){
        clearInterval(myInterval)
    }
    else{
        pos += 1
        animate.style.left = pos + 'px'
    }    
}