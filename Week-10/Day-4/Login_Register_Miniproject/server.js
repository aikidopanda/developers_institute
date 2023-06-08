const express = require('express')
const dotenv = require('dotenv')
const {client} = require('./db')
const p4ssw0rd = require('p4ssw0rd')
const pg = require('pg')
client.connect()

let app = express()
dotenv.config()

app.use(express.static(__dirname + '/public'))
app.use(express.urlencoded({express:true}))

app.listen(process.env.PORT || 3001, () => {
    console.log('running on port 3001')
})

app.get('/signup', (req,res)=>{
    res.sendFile(__dirname + '/public/signup.html')
})

app.post('/login', (req,res)=>{
    let username = req.body.username
    let password = req.body.password

    getCredentials(username)
    .then((result) => {
        user = result.rows[0].username
        hashed = result.rows[0].password

        if (p4ssw0rd.check(password, hashed)){
            res.send('You have logged in!')
        }
        else{
            res.send('Invalid password!')
        }
    })
    .catch(() => {
        res.send('There is no such user in database.')
    })
})

app.post('/register', (req,res)=>{
    let fname = req.body.fname
    let lname = req.body.lname
    let username = req.body.username
    let email = req.body.email
    let password = p4ssw0rd.hash(req.body.password)

    let userId
    getId(email)
    .then((result) => {
        userId = result.rows[0].id
        console.log(userId)
        if (userId){
            res.send(`This email is already used!`)
        }
    })
    .catch(() => {
        register(fname, lname, username, email, password)
        getId(email)
        .then((result) => {
            userId = result.rows[0].id
            res.send(`You have registered! Your id is ${userId}`)
        })
    })
})

async function register(fname, lname, username, email, password){
    try {
        await client.query(`insert into users (fname, lname, username, email, password)
        values ('${fname}', '${lname}', '${username}', '${email}', '${password}')`)
    } catch (error) {
        console.log(error)
    }
}

async function getId(email){
    try {
        let id = await client.query(`select id from users where email='${email}'`)
        return id
    }
    catch (error){
        console.log(error)
    }
}

async function getCredentials(username){
    try {
        let res = await client.query(`select username, password from users where username='${username}'`)
        return res
    }
    catch (error){
        console.log(error)
    }
}