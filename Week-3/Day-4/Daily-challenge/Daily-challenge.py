#simple way, maybe I was kinda cheating
matrix = [
    ['7','T','h','i','s','$','#','^'],
    ['i','s','%',' ','M','a','t','r'],
    ['3','i','x','#',' ',' ','%','!']
]
final=''
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j].isalpha():
            final += matrix[i][j]
        elif matrix[i][j-1].isalpha():
            final += ' '
print (final)

# hard way
matrix1 = [
    ['7','i','3'],
    ['T','s','i'],
    ['h','%','x'],
    ['i',' ','#'],
    ['s','M',' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^','r','!']
]
final = ''
i = 0
j = 0
while 0 <= j <= len(matrix1[0]) - 1:
    while i < len(matrix1):
        if matrix1[i][j].isalpha():
            final += matrix1[i][j]
        elif matrix1[i][j].isnumeric():
            final += ''
        else:
            final += ' '
        i += 1
    j += 1
    i = 0
final = ' '.join(final.split())



print(final)
        
        

