//I did this mini-project differently. Instead of giving random results I tried to build a search form when user can specify both the category and name of object he wants to fing

let form = document.forms[0]
let selectInput
let searchInput
let searchId

let searchButton = document.getElementById('search-button')
form.addEventListener('submit',search)

async function search(event){
    event.preventDefault()
    selectInput = form.selection.value
    searchInput = form.inputtext.value
    let container = document.getElementsByClassName('info-container')[0]
    container.innerHTML = '<p>Loading...</p><i class="fa-solid fa-spinner fa-spin-pulse fa-spin-reverse"></i>'
    console.log(selectInput)

    let url = `https://www.swapi.tech/api/${selectInput}/`
    let response = await fetch(url)
    if (response.status == 200){
        let json = await response.json()
        let results = json.results
        for (item of results){
            if (item.name == searchInput){
                searchId = item.uid
            }
        }

        let url1 = `https://www.swapi.tech/api/${selectInput}/${searchId}`
        let response1 = await fetch(url1)
        if (response1.status == 200){
            let json1 = await response1.json()
            let result = json1.result.properties
            console.log(result)

            if (selectInput == 'people'){
                let response2 = await fetch(result.homeworld)
                let json2 = await response2.json()
                let home = json2.result.properties.name

                container.innerHTML = `
                <p id='name'>${result.name}</p>
                <p>Height: ${result.height}</p>
                <p>Gender: ${result.gender}</p>
                <p>Birth year: ${result.birth_year}</p>
                <p>Homeworld: ${home}</p>`
            }
            else if(selectInput == 'planets'){
                container.innerHTML = `
                <p id='name'>${result.name}</p>
                <p>Population: ${result.population}</p>
                <p>Terrain: ${result.terrain}</p>
                <p>Climate: ${result.climate}</p>
                <p>Gravity: ${result.gravity}</p>`
            }
            else if(selectInput == 'starships'){
                container.innerHTML = `
                <p id='name'>${result.name}</p>
                <p>Class: ${result.starship_class}</p>
                <p>Cost in credits: ${result.cost_in_credits}</p>
                <p>Manufacturer: ${result.manufacturer}</p>`
            }        
        }

        else{
            container.innerHTML = `<p>There is no such ${selectInput} in our database!</p>`         
            throw new Error(`There is no ${selectInput} in given category`)
        }
    }
}


