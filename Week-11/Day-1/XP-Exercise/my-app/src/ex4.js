import './ex4.css'
const MyComp = () => {
    const style_header = {
        color: "white",
        backgroundColor: "DodgerBlue",
        padding: "10px",
        fontFamily: "Arial"
      };

    return(
        <>
        {/* <h1 style={{color: 'red', backgroundColor: 'lightblue'}}>Hello World</h1> */}
        <h1 style={style_header}>Hello World</h1>
        <p className='para'>Some text</p>
        <a href="www.google.com">Google link</a>
        <form>
            <input placeholder="Enter your name"/>
            <input type="email" placeholder="And an email"/>
            <input type="submit" value="Submit"/>
        </form>
        <ol>
            <li>First item</li>
            <li>Second item</li>
        </ol>
        <img src="france.jfif"/>
        </>
    )
}

export default MyComp