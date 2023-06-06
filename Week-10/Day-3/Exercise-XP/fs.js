//Exercise 1
const fs = require('fs')
fs.readFile('sample.txt', 'utf-8', (err, data) => {
    console.log(data)
})

//Exercise 2
fs.writeFile('data.txt', 'Sample string', (err)  => {
    if (err){
        throw err
    }
    console.log('File was created')
}
)

fs.appendFile('data.txt', '\nOne more sample string', (err)  => {
    if (err){
        throw err
    }
    console.log('File was edited')
}
)

fs.unlink('data.txt', (err)  => {
    if (err){
        throw err
    }
    console.log('File deleted')
}
)


