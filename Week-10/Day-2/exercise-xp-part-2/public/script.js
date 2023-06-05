let data
async function fetcher(){
    let response = await fetch('http://localhost:3000/temp/')
    let json = response.json()
    return json
}

async function main(){
    data = await fetcher()
    console.log(data)
    document.querySelector('body').innerText = JSON.stringify(data)
}
main()

// fetcher().then((result) => console.log(result))




