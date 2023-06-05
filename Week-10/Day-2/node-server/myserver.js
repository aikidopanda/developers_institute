let http = require('http')

const hostname = 'localhost'
const port = 3000

const server = http.createServer( (req,res) => {
    res.setHeader('Content-Type', 'text/html')
    res.writeHead(200);
    res.end(`
    <html>
    <body>
    <h1>This is my first response</h1>
    <h2>This is my second response</h2>
    <p>This is my third response</p>
    </body>
    </html>`)
})

server.listen(3000, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`)
})