const User = (props) => {
  const {userinfo} = props;
  const {id, name, email, username, phone} = userinfo;
  return (
    <div>
      <img src={`https://robohash.org/${id}?size=150x150`} />
      <h2>{name}</h2>
      <p>{email}</p>
      <p>{username}</p>
      <p>{phone}</p>
    </div>
  )
}

export default User
