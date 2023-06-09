//Exercise 1
function compareToTen(num){
    let myPromise = new Promise( function(resolve,reject){
        if (num < 10){
            resolve('Success')
        }
        else{
            reject('Failure')
        }
    }   
    )
    return myPromise
}

compareToTen(8)
.then(result => console.log(result))
.catch(error => console.log(error))

//Exercise 2
let myPromise = new Promise( function(resolve,reject){
    if (true){
        setTimeout(()=> {
            resolve('Success!')
        },'4000')
    }
    else{ // just a placeholder in this case
        reject(
            console.log('OOPS, something went wrong!')
        )
    }
} )
myPromise.then(result=>console.log(result))
myPromise.catch(error=>console.log(error))

//shorter way
let myRes
setTimeout(()=> {
    myRes = Promise.resolve('Success!'); myRes.then(result=>console.log(result))
},'4000')

//Exercise 3
let switcher = false // for testing purpose
let newPromise = new Promise( function(resolve,reject){
    if (switcher == true){
        resolve(3)
    }
    else{
        reject('Boo!')
    }
})
.then(result=>console.log(result))
.catch(error=>console.log(error))
//another way
let myVar1 = Promise.resolve(3)
let myVar2 = Promise.reject('boo')
console.log(myVar1, myVar2)
