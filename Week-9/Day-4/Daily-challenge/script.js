let url_global = 'https://v6.exchangerate-api.com/v6/58a1d8a4db5ebc675579c1f0/codes'

async function getCurrencyList(){
    let response = await fetch(url_global)
    let json = await response.json()
    for (item of json.supported_codes){
        
        let opt = document.createElement('option')      
        opt.value = item[0]
        opt.innerText = item[1]

        let opt1 = document.createElement('option') // Repeat looks stupid but it seems we cant append the same element to different parents...    
        opt1.value = item[0]
        opt1.innerText = item[1]

        document.getElementById('currency_from').appendChild(opt)
        document.getElementById('currency_to').appendChild(opt1)
    }
}
getCurrencyList()

let form = document.forms[0]
form.addEventListener('submit',exchange)

let curFrom
let curTo

async function exchange(event){
    event.preventDefault()
    curFrom = form.currency_from.value
    curTo = form.currency_to.value
    let amount = form.amount.value
    let url_pairs = `https://v6.exchangerate-api.com/v6/58a1d8a4db5ebc675579c1f0/pair/${curFrom}/${curTo}`

    let response = await fetch(url_pairs)
    let json = await response.json()
    let rate = json.conversion_rate

    let amountNew = amount * rate
    let newPar = document.createElement('p')
    newPar.innerText = `You will get ${amountNew} ${curTo} for ${amount} ${curFrom}`
    sectionRes = document.getElementById('results')
    sectionRes.appendChild(newPar)
}

let btn = document.querySelector('button')
btn.addEventListener('click', switcher)

function switcher(){
    let temp = form.currency_from.value
    let temp1 = form.currency_to.value
    form.currency_to.value = temp
    form.currency_from.value = temp1
}
