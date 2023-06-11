const express = require('express')
const p4ssw0rd = require('p4ssw0rd')
const fs = require('fs')
let registerValid = true

let app = express()

app.use(express.static(__dirname + '/public'))
app.use(express.urlencoded({express:true}))

app.listen(process.env.PORT || 3001, () => {
    console.log('running on port 3001')
})

app.get('/login/', (req,res)=>{
    res.sendFile(__dirname + '/public/login.html')
})

app.get('/register/', (req,res)=>{
    res.sendFile(__dirname + '/public/registration.html')
})

app.get('/fetch',(req,res)=>{
    res.send(registerValid)
})

app.post('/register', (req, res)=>{
    let newUser = {
        'fname': req.body.fname,
        'lname': req.body.lname,
        'username': req.body.username,
        'email': req.body.email,
        'password': p4ssw0rd.hash(req.body.password)
    }
    registerUser(newUser)
    res.sendFile(__dirname + '/public/registration.html')
})

function registerUser(obj){

    let usersList = []
    let newUserJson

    fs.readFile('users.json',(err,data)=>{
        if (err){
            console.log(err)
        }
        else{
            usersList = JSON.parse(data) || []
            usersList.push(obj)
            newUserJson = JSON.stringify(usersList)
            registerValid = true
            console.log(usersList)
            fs.writeFile('users.json', newUserJson, (err) => {
                if (err){
                    console.log(err)
                }
                console.log('A new user has been registered')
            })
        }
    })
}