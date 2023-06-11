const FavoriteColors = (props) => {
    console.log(props.animals)
    return (
        <ul>
            {props.animals.map((item, i) => {
                return <li key={i}>{item}</li>
            })}
        </ul>
    )
}

export default FavoriteColors