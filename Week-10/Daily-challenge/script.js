const main = require('./main')

let number = main.largeNumber

let datetime = main.getDate()
let months = ['January', 'February', 'March', 'April', 'May', 'June',
'July', 'August', 'September', 'October', 'November', 'December']

let b = 5

console.log(number + b)

const hostname = '127.0.0.1'
const port = 3000

let http = require('http')

let server
let server1

// server = http.createServer( (req,res)=>{
//     res.setHeader('Content-Type', 'text/html')
//     res.writeHead(200);
//     res.end(`<html><body>
//     <h1>Hi there at the frontend</h1>
//     <p>My Module is ${number}</p>
//     </body></html>`);
// })

server1 = http.createServer( (req,res)=>{
    res.setHeader('Content-Type', 'text/html')
    res.writeHead(200);
    res.end(`<html><body>
    <h1>Hi there at the frontend</h1>
    <p>Today is ${months[datetime.month - 1]} ${datetime.day} ${datetime.year}. It's ${datetime.hour}:${datetime.minute}:${datetime.second} now.</p>
    </body></html>`);
})
if (server){
    server.listen(port, hostname, () => {
        console.log(`Server running at http://${hostname}:${port}/`)
    })
}
if (server1){
    server1.listen(port, hostname, () => {
        console.log(`Server running at http://${hostname}:${port}/`)
    })
}

