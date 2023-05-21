// //Exercise 1
// let select = document.getElementById('genres')
// console.log(select.value)

// let newOption = new Option('Classic','classic')
// select.add(newOption)
// select.value = 'classic'

// //Exercise 2
// let form = document.querySelector('form')
// let elements = form.elements
// let colorSelect = elements[0]
// let button = elements[1]
// console.log(elements)
// // let colorSelect = document.getElementById('colorSelect')
// console.log(colorSelect)
// function removeColor(){
//     colorSelect.options.remove(colorSelect.selectedIndex)
// }
// button.addEventListener('click',removeColor)

//Exercise 3
shoppingList = []
myForm = document.createElement('form')
textInput = document.createElement('input'); textInput.setAttribute('type', 'text')
button = document.createElement('button'); button.innerText = 'Add Item'
buttonClear = document.createElement('button'); buttonClear.innerText = 'Clear all'
myForm.appendChild(textInput); myForm.appendChild(button); myForm.appendChild(buttonClear)
root.append(myForm)

function addItem(event){
    if (textInput.value.length > 0){
        shoppingList.push(textInput.value)
        textInput.value = ''
        console.log(shoppingList)
    } 
    event.preventDefault()
}

function clearAll(event){
    shoppingList = []
    console.log(shoppingList)
    event.preventDefault()
}

button.addEventListener('click', addItem)
buttonClear.addEventListener('click', clearAll)