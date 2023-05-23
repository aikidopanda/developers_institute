//Exercise 1
//output will be 2,4,6

//Exercise 2
// output: [1, 2, 0, 1, 2, 3], first reduce gives 0,1,2,3

//Exercise 3
// i will be equal to the index of the current num

//Exercise 4
const array = [[1],[2],[3],[[[4]]],[[[5]]]]
let newarr = array.flat(2)
console.log(newarr)
const greeting = [["Hello", "young", "grasshopper!"], ["you", "are"], ["learning", "fast!"]]
let newgreeting = greeting.flat()
console.log(newgreeting)
let greetingStr = newgreeting.join(' ')
console.log(greetingStr)

const trapped = [[[[[[[[[[[[[[[[[[[[[[[[[[3]]]]]]]]]]]]]]]]]]]]]]]]]]
let freed = trapped.flat(Infinity)
console.log(freed)

