let http = require('http')

const hostname = 'localhost'
const port = 8080

let obj = {
    firstname: 'John',
    lastname: 'Doe'
}
let json = JSON.stringify(obj)

const server = http.createServer( (req,res) => {
    res.setHeader('Content-Type', 'text/html')
    res.end(json)
})

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`)
})