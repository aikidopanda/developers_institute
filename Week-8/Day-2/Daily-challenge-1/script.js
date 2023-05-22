const gameInfo = [
    {
      username: "john",
      team: "red",
      score: 5,
      items: ["ball", "book", "pen"]
    },
    {
      username: "becky",
      team: "blue",
      score: 10,
      items: ["tape", "backpack", "pen"]
    },
    {
      username: "susy",
      team: "red",
      score: 55,
      items: ["ball", "eraser", "pen"]
    },
    {
      username: "tyson",
      team: "green",
      score: 1,
      items: ["book", "pen"]
    },
   ];

let usernames = []
gameInfo.forEach(function(item){
    usernames.push(item.username + '!')
})
console.log(usernames)

let winners = []
gameInfo.forEach(function(item){
    if (item.score > 5){
        winners.push(item.username)
    } 
})
console.log(winners)

let totalScore = 0
gameInfo.forEach(function(item){
    totalScore += item.score 
})
console.log(totalScore)

