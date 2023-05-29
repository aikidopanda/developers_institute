//Exercise 1

const promise1 = Promise.resolve(3);
const promise2 = 42;
const promise3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 3000, 'foo');
});

Promise.all([promise1, promise2, promise3]).then((values) => {
    console.log(values);
  });
//Promise.all() takes a group of promises and returns an array of fulfillment(resolve) values when all of these promises are fulfilled

//Exercise 2
//The output will be an array [2,4,6] since all the promises are fulfilled and the function just multiplies every element by 2