import random
mylist=["hello","hola","Nǐ hǎo","Konnichiwa"]
greeting=random.choice(mylist)
print(greeting+" im dev")

row=int(input("enter row: "))
col=int(input("enter column: "))
emojiGrid=[]

for i in range(row):
    rowList=[]
    for j in range(col):
        rowList.append('😂 ')
    emojiGrid.append(rowList)

for i in range(row):
    for j in range(col):
        print(emojiGrid[i][j],end=" ")
    print()