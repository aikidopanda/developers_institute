// //Exercise 1
// let express = require('express')
// let app = express()
// app.listen(3000, () => {
//     console.log('Server is running on port 3000')
// })
// app.use(express.static('public',
// {
//   setHeaders: (res, path) => {
//     if (path.endsWith('.js')) {
//       res.setHeader('Content-Type', 'text/javascript');
//     }
//   }
// }))

// const server = app.get('/', (req, res) => {
//     const user = {
//         firstname: 'John',
//         lastname: 'Doe'
//     }
//     res.json(user)
// })

// app.get('/temp', (req, res) => {
//     const user = {
//         firstname: 'John',
//         lastname: 'Doe'
//     }
//     res.json(user)
// })

//Exercise 2

// let express = require('express')
// let app = express()
// app.listen(3000, () => {
//     console.log('Server is running on port 3000')
// })
// app.get('/test/:id/', (req, res) => {
//     console.log(req.params)
//     res.send(req.params)
// })

//Exercise 3
let express = require('express')
let app = express()
app.listen(3000, () => {
    console.log('Server is running on port 3000')
})
app.use(express.static('public-ex-3',
{
  setHeaders: (res, path) => {
    if (path.endsWith('.js')) {
      res.setHeader('Content-Type', 'text/javascript');
    }
  }
}))
