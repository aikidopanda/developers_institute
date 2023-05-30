//Exercise 1 is technically the same as daily challenge so I think it's already done

//Exercise 2
//first, 'starting slow promise' will appear
//after 2 sec it will print 'slow' and 'starting fast promise'
// after 1 sec it will print 'fast promise is done' and 'fast'

//Exercise 3
//In this case function are synchronous so the 'fast' function will wait until the 'slow' one is resolved

//Exercise 4
const urls = [
    "https://jsonplaceholder.typicode.com/users",
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/albums"
  ];

const getData = async function() {
    try{
        const [ users, posts, albums ] = await Promise.all(urls.map(url =>
        fetch(url)
        ));
        newArr = []
        for (item of [ users, posts, albums ]){
            let temp = await item.json()
            newArr.push(temp)
        }

        console.log('users', newArr[0]);
        console.log('posta', newArr[1]);
        console.log('albums', newArr[2]);
    }
    catch(e){
        console.error(e)
    }
}


getData()