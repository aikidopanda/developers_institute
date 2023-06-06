let express = require('express')
let bodyParser = require('body-parser')
let app = express()
let urlencodedParser = bodyParser.urlencoded({ extended: false })
let email
let msg
app.listen(3000, () => {
    console.log('Server is running on port 3000')
})
app.use(express.static('public'))

app.get('/aboutme/:hobby', (req,res) => {
    let hobby = req.params.hobby
    let pattern = (/^[A-Za-z]+$/) // dont know how to do this task without regex, 'typeof' doesnt work because if user
    // enters numbers they are regarded as a string anyway
    if (!hobby.match(pattern)){
        res.status(404).send('Not found')
    }
    else{
        res.send(`<p>My hobby is ${hobby}</p>`)
    }
})

app.get('/pic/', (req,res) => {
    let pictureSrc = __dirname + '/public/some_cat_image.webp'
    res.send(`<img src="/public/some_cat_image.webp" width="300">`) // I dont understand how to send images with this command, always get the path error
})

app.get('/form', (req,res) => {
    res.sendFile(__dirname + '/public/index.html')
})

app.post('/form', urlencodedParser, (req,res) => {
    email = req.body.email
    msg = req.body.msg
    res.send(`
    <p>You sent a message!</p>
    `)
})

app.get('/formdata', (req,res) => { 
    res.send(`
    <p>${email} has sent you a message: ${msg}</p>
    `)
})