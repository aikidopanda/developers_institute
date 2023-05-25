const robots = [
    {
      id: 1,
      name: 'Leanne Graham',
      username: 'Bret',
      email: 'Sincere@april.biz',
      image: 'https://robohash.org/EVN.png?set=set1&size=150x150'
    },
    {
      id: 2,
      name: 'Ervin Howell',
      username: 'Antonette',
      email: 'Shanna@melissa.tv',
      image: 'https://robohash.org/L7I.png?set=set1&size=150x150'
    },
    {
      id: 3,
      name: 'Clementine Bauch',
      username: 'Samantha',
      email: 'Nathan@yesenia.net',
      image: 'https://robohash.org/GN2.png?set=set1&size=150x150'
    },
    {
      id: 4,
      name: 'Patricia Lebsack',
      username: 'Karianne',
      email: 'Julianne.OConner@kory.org',
      image: 'https://robohash.org/GON.png?set=set1&size=150x150'
    },
    {
      id: 5,
      name: 'Chelsey Dietrich',
      username: 'Kamren',
      email: 'Lucio_Hettinger@annie.ca',
      image: 'https://robohash.org/Q7J.png?set=set1&size=150x150'
    },
    {
      id: 6,
      name: 'Mrs. Dennis Schulist',
      username: 'Leopoldo_Corkery',
      email: 'Karley_Dach@jasper.info',
      image: 'https://robohash.org/Y05.png?set=set1&size=150x150'
    },
    {
      id: 7,
      name: 'Kurtis Weissnat',
      username: 'Elwyn.Skiles',
      email: 'Telly.Hoeger@billy.biz',
      image: 'https://robohash.org/QFF.png?set=set1&size=150x150'
    },
    {
      id: 8,
      name: 'Nicholas Runolfsdottir V',
      username: 'Maxime_Nienow',
      email: 'Sherwood@rosamond.me',
      image: 'https://robohash.org/GOC.png?set=set1&size=150x150'
    },
    {
      id: 9,
      name: 'Glenna Reichert',
      username: 'Delphine',
      email: 'Chaim_McDermott@dana.io',
      image:'https://robohash.org/QBT.png?set=set1&size=150x150'
    },
    {
      id: 10,
      name: 'Clementina DuBuque',
      username: 'Moriah.Stanton',
      email: 'Rey.Padberg@karina.biz',
      image:'https://robohash.org/IDM.png?set=set1&size=150x150'
    }
    ];

function createGrid(array){
    for (item of array){
        let newdiv = document.createElement('div')
        newdiv.classList.add('robot'); newdiv.id = item.name
        let robotPicture = document.createElement('img'); robotPicture.src = item.image; robotPicture.classList.add('robot_pic')
        let robotName = document.createElement('p'); robotName.innerText = item.name; robotName.classList.add('name')
        let robotEmail = document.createElement('p'); robotEmail.innerText = item.email; robotEmail.classList.add('email')
        newdiv.appendChild(robotPicture); newdiv.appendChild(robotName); newdiv.appendChild(robotEmail)
        document.getElementById('container-main').appendChild(newdiv)
    }
}

window.onload = createNavElements(), createGrid(robots)
function createNavElements(){
    let title = document.createElement('p'); let search = document.createElement('input')
    title.id = 'title'; title.innerText = 'Robofriends'
    search.type = 'text'; search.placeholder = 'Search robots by name'; search.id = 'search'
    document.querySelector('nav').appendChild(title); document.querySelector('nav').appendChild(search)
}

let search = document.getElementById('search')
search.addEventListener('input', robotFilter)

function robotFilter(event){
    if (event.target.value.length > 0){
        let filtered = robots.filter(item => item.name.toLowerCase().includes(event.target.value.toLowerCase()))
        let images = document.getElementsByClassName('robot')
        for (item of images){
            item.style.display = 'none'
        }
        createGrid(filtered)
    }
    else{
        location.reload()
    }
}

