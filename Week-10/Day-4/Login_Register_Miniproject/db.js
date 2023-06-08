const knex = require('knex');
const dotenv = require('dotenv');
const { Client } = require('pg');

dotenv.config()

const client = new Client({
    user: process.env.DB_USER,
    host: process.env.DB_HOST,
    database: process.env.DB_NAME,
    password: process.env.DB_PASSWORD,
    port: process.env.DB_PORT,
    ssl:{rejectUnauthorized:false}
})


// const connectDb = async () => {
//     try {
//         const client = new Client({
//             user: process.env.DB_USER,
//             host: process.env.DB_HOST,
//             database: process.env.DB_NAME,
//             password: process.env.DB_PASSWORD,
//             port: process.env.DB_PORT,
//             ssl:{rejectUnauthorized:false}
//         })
 
//         await client.connect()
//         const res = await client.query('SELECT * FROM users')
//         console.log(res.rows)
//         await client.end()
//     } catch (error) {
//         console.log(error)
//     }
// }

// connectDb()
  
  module.exports = {
    client
  }