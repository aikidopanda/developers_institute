import React from 'react';

class HelloClass extends React.Component {
  // constructor(){
  //   super()
  // }
  render(){
    const products = [
      {name:'apple'},{name:'orange'},{name:'banana'}
    ]
    return (
      <>
        {
          products.map((item, i)=>{
            return (
              <div key={i}>
                {item.name}
              </div>
            )
          })
        }
      </>
    )
  }
}

export default HelloClass
