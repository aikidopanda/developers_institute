let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        payed : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

let displayGroceries = () => groceries.vegetables.forEach(item => console.log(item))
displayGroceries();

let cloneGroceries = () => user = client; client = 'Betty'; shopping = groceries; groceries.totalPrice = '35$'; groceries.payed = false;
cloneGroceries() // user is also Betty
console.log(user,client)
console.log(shopping.totalPrice, shopping.payed, groceries.totalPrice, groceries.payed)// original objects are also affected just because js works this way I guess. To clone objects we need another syntax