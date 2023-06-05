let express = require('express')

let app = express()
app.listen(3001, () => {
    console.log('Server is running on port 3001')
})

app.get('/', (req,res) => {
    res.send(`<html><h1>This is an HTML tag</h1></html>`)
})
