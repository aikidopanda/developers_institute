let allBooks = [
    {
        title: 'Lord of the Rings',
        author: 'John Ronald Ruel Tolkien',
        image: 'lotr.jpg',
        alreadyRead: true,
    },
    {
        title: 'Infinite Jest',
        author: 'David Foster Wallace',
        image: 'jest.jpg',
        alreadyRead: false,
    }
]

section = document.querySelector('section')

for (let item in allBooks){
    let div = document.createElement('div')
    let par = document.createElement('p')
    let partxt = document.createTextNode(allBooks[item].title)
    par.append(partxt)
    let par1 = document.createElement('p')
    let partxt1 = document.createTextNode(allBooks[item].author)
    par1.append(partxt1)
    let img = document.createElement('img')
    img.src = allBooks[item].image
    img.style.width = '100px'
    div.appendChild(par)
    div.appendChild(par1)
    div.appendChild(img)
    if (allBooks[item].alreadyRead == true){
        div.style.backgroundColor = 'red'
    }
    section.appendChild(div)
}