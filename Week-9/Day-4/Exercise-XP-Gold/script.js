let form = document.forms[0]
form.addEventListener('submit',findPokemon)
let urlGlobal = 'https://pokeapi.co/api/v2/pokemon/'

let sectionImage = document.getElementById('pokemon_image')
let sectionInfo = document.getElementById('pokemon_info')

async function findPokemon(event){
    event.preventDefault()
    sectionInfo.innerHTML = 'Loading...'
    let response = await fetch(urlGlobal)

    if (response.status == 200){
        let json = await response.json()
        let pokeList = json.results

        let randomizer = Math.floor(Math.random() * pokeList.length)
        let pokeName = pokeList[randomizer].name

        let url1 = `https://pokeapi.co/api/v2/pokemon/${pokeName}`
        let response1 = await fetch(url1)
            if (response1.status == 200){
                let json1 = await response1.json()
                console.log(json1)

                for (item of sectionImage.children){
                    sectionImage.removeChild(item)
                }

                let img = document.createElement('img')
                img.src = json1.sprites.front_default
                sectionImage.appendChild(img)

                let types = ''
                for (item of json1.types){
                    console.log(item.type)
                    types = types + item.type.name + ';'
                }

                sectionInfo.innerHTML = `<p>${json1.name}</p>
                <p>Pokemon №${json1.id}</p>
                <p>Height: ${json1.height} cm</p>
                <p>Weight: ${json1.weight} pounds</p>
                <p>Types: ${types}`
            }
    }    
}