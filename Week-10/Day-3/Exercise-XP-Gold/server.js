const express = require('express')
const fs = require('fs')

let app = express()
app.use(express.static('/public'))

let bodyParser = require('body-parser')
let urlencodedParser = bodyParser.urlencoded({ extended: false })

app.listen(3000, () => {
    console.log('Server is running on port 3000')
})

let itemsLength
let jsonData

app.get('/items', (req,res) => {
    fs.readFile('store.json', 'utf-8', (err, data) => {
        if (err){
            console.log(err)
            return
        }
        jsonData = JSON.parse(data)
        res.json(jsonData)
    })
})

app.get('/items/:id', (req,res) => {
    fs.readFile('store.json', 'utf-8', (err, data) => {
        if (err){
            console.log(err)
            return
        }
        jsonData = JSON.parse(data)
        console.log(jsonData)
        let itemFound = jsonData.find((item) => item.id == req.params.id)
        res.send(itemFound)
    })
})

app.get('/additems', (req,res) => {
    fs.readFile('store.json', 'utf-8', (err, data) => {
        if (err){
            console.log(err)
            return
        }
        jsonData = JSON.parse(data)
        itemsLength = jsonData.length
    })
    res.sendFile(__dirname + '/public/index.html')
})

app.post('/additems', urlencodedParser, (req, res) => {
    let newItem = {
        id: itemsLength + 1,
        name: req.body.name,
        price: req.body.price
    }
    jsonData.push(newItem)
    let newJson = JSON.stringify(jsonData)
    fs.writeFile('store.json', newJson, (err) => {
        if (err){
            console.log(err)
            return
        }      
    })
    res.send('New item has been added!')
})


