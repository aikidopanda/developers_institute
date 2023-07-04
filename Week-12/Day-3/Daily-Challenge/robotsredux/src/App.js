import logo from './logo.svg';
import './App.css';
import UserClass from './components/UserClass';
import robots from './users.json';

// console.log(robots);

function App() {

  return (
    <div>
      <header>
        {
          robots.map((item,indx) => {
            return <UserClass userinfo={item} key={indx}/>
          })
        }
      </header>
    </div>
  );
}

export default App;
