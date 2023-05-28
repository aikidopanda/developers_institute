const quotes = [
    {
        'id': 0,
        'author': 'William Shakespeare',
        'quote': 'The world is a theater and people are its actors',
        'likes': 0
    },
    {
        'id': 1,
        'author': 'Julius Caesar',
        'quote': 'Veni vidi vici',
        'likes': 0
    },
    {
        'id': 2,
        'author': 'Winston Churchill',
        'quote': 'Dogs look up to you, cats look down on you. Give me a pig. He just looks you in the eye and treats you as an equal.',
        'likes': 0
    },
    {
        'id': 3,
        'author': 'Winston Churchill',
        'quote': 'Success is a move from one failure to another without losing enthusiasm',
        'likes': 0
    }
]

let prevIndex
let generatedQuote
let quoteIndex
let quoteWindow = document.getElementById('quote-window')

buttonGen = document.getElementById('generate')
buttonGen.addEventListener('click', quoteGen)

function quoteGen(){
    quoteIndex = Math.floor(Math.random() * quotes.length)
    if (quoteIndex == prevIndex){
        quoteGen()
    }
    else{
        for (item of quoteWindow.children){
            quoteWindow.removeChild(item)
        }
        generatedQuote = document.createElement('p')
        generatedQuote.innerText = quotes[quoteIndex].quote + '\n' + quotes[quoteIndex].author
        quoteWindow.appendChild(generatedQuote)
        prevIndex = quoteIndex
    }
}

submitQuote = document.getElementById('submit-quote');
submitQuote.addEventListener('click', addQuote)

function addQuote(event){
    let form = document.forms[1]
    let newQuote = {
        'id': quotes.length,
        'author': form.author.value,
        'quote': form.quote.value,
        'likes': 0
    }
    quotes.push(newQuote)
    console.log(quotes)
    event.preventDefault()
}

buttonLengthSpace = document.getElementById('length-space'); 
buttonLengthSpace.addEventListener('click', calcLengthSpace);

buttonLengthNoSpace = document.getElementById('length-no-space'); 
buttonLengthNoSpace.addEventListener('click',calcLengthNoSpace)

buttonWords = document.getElementById('words-num'); 
buttonWords.addEventListener('click', calcWords)

buttonLike = document.getElementById('like'); 
buttonLike.addEventListener('click',like)

buttonSearch = document.getElementById('search'); 
buttonSearch.addEventListener('click',search)



function calcLengthSpace(){
    let newpar = document.createElement('p')
    newpar.innerText = `This quote has ${generatedQuote.innerText.length} characters`
    document.getElementById('additional-info').appendChild(newpar)
}

function calcLengthNoSpace(){
    let quoteLength = 0
    for (char of generatedQuote.innerText){
        if (char != ' '){
            quoteLength++
        }
    }
    let newpar = document.createElement('p')
    newpar.innerText = `This quote has ${quoteLength} characters without space`
    document.getElementById('additional-info').appendChild(newpar)
}

function calcWords(){
    let wordsNum = 0
    for (char of generatedQuote.innerText){
        if (char == ' '){
            wordsNum++
        }
    }
    let newpar = document.createElement('p')
    newpar.innerText = `This quote has ${wordsNum} words`
    document.getElementById('additional-info').appendChild(newpar)
}

function like(){
    quotes[quoteIndex].likes ++
    alert(`You liked this quote! Now it has ${quotes[quoteIndex].likes} likes`)
}

function search(event){
    let form = document.forms[0]
    console.log(form)
    let filtered = quotes.filter((item) => item.author.includes(form.searchfield.value))
    if (form.searchfield.value.length > 0){
        for (item of quoteWindow.children){
            quoteWindow.removeChild(item)
        }
       for (item of filtered){
           let newQuote = document.createElement('p')
           newQuote.innerText = item.quote + '\n' + item.author
           quoteWindow.appendChild(newQuote)
       }
    }  
    event.preventDefault()
}

//Dont forget to add previous and next buttons for searched author