
(function(username, picturePath){
    newdiv = document.createElement('div')
    divtxt = document.createTextNode(username)
    newdiv.append(divtxt)
    document.querySelector('nav').appendChild(newdiv)
    img = document.createElement('img')
    img.src = picturePath
    img.style.height = '50px';img.style.width = '50px'
    document.querySelector('nav').appendChild(img)
})('Alex','avatar.jfif')