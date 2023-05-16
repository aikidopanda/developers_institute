let line =''

for (let i = 0; i < 6; i++){
    line = line + '*'
    console.log(line)
}

//nested loop, looks like too hard solution for too simple task
let newline =''
for (let i = 0; i < 6; i++){
    for (let j = 0; j < 1; j++){
        newline = newline + '*'
    }
    console.log(newline)
}