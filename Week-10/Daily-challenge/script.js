const main = require('./main')

let number = main.largeNumber

let b = 5

console.log(number + b)

const hostname = '127.0.0.1'
const port = 3000

let http = require('http')

const server = http.createServer( (req,res)=>{
    res.setHeader('Content-Type', 'text/html')
    res.writeHead(200);
    res.end(`<html><body>
    <h1>Hi there at the frontend</h1>
    <p>My Module is ${number}</p>
    </body></html>`);
})
server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`)
})
