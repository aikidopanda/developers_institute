// Probably I get it wrong but all the exercises can be done with almost the same code.

//Exercise 1

let url = 'https://api.giphy.com/v1/gifs/search?q=funny&limit=20&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'

async function getData(){
    let response = await fetch(url)
    if (response.status == 200){
        const json = await response.json()
        console.log(json.data)
    }
    else{
        throw new Error('Something is wrong with the query') 
    }
}

getData()
.catch(console.error)
.then(() => console.log('Just to ensure that error doesnt block the following code'))

//Exercise 2

let url2 = 'https://api.giphy.com/v1/gifs/search?q=sun&limit=10&offset=2&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'
//just manually changed the url i am sure there is a better way but I dont get it yet

async function getDataNew(){
    let response = await fetch(url2)
    if (response.status == 200){
        const json = await response.json()
        console.log(json.data)
    }
    else{
        throw new Error('Something is wrong with the query') 
    }
}

getDataNew()
.catch(console.error)
.then(() => console.log('Just to ensure that error doesnt block the following code'))

//Exercise 3
// improve this code
// fetch("https://www.swapi.tech/api/starships/9/")
//     .then(response => response.json())
//     .then(objectStarWars => console.log(objectStarWars.result));

async function myFetcher(){
    let url = "https://www.swapi.tech/api/starships/9"
    let response = await fetch(url)
    if ( response.status == 200){
        let json = await response.json()
        console.log(json.result.properties) 
    }   
    else{
        throw new Error('Something is wrong with the query') 
    }
}
myFetcher()
.catch(console.error)

//Exercise 4
// The output is a promise that is going to be resolved after 2 seconds, because asyncCall() function is calling resolveAfter2Seconds() which returns this 2sec promise

