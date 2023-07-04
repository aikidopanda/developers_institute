import './Hello.css'
import React from 'react'
import HelloClass from './HelloClass'

const Hello = () => {
  const users = [
    {
      name: 'Mary',
      email: 'mary@gmail.com',
      id: 1
    },
    {
      name: 'John',
      email: 'john@gmail.com',
      id: 2
    },
    {
      name: 'David',
      email: 'david@gmail.com',
      id: 3
    }
  ]
  const styling = {
    textAlign:'center',
    display:'inline-block',
    padding:'20px',
    margin:'20px',
    border:'1px solid #ccc'
  }
  const returnusers = users.map((item, i) => {
    return (
      <div key={i} style={{
        textAlign:'center',
        display:'inline-block',
        padding:'20px',
        margin:'20px',
        border:'1px solid #ccc'
      }}>
        <h4 className="title">{item.name}</h4>
        <p>{item.email}</p>
      </div>
    )
  })
  return (
    <>
      <h1> Hello, </h1>
      {
        returnusers
      }
      <HelloClass />
    </>
  )
}

export default Hello
