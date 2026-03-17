dic={}
while True:
  print("1. add subject and marks")
  print("2. view subject and marks")
  print("3. Exit")
  userIn=int(input("enter your choice(1-3):"))
  if userIn==1:
    word=input("Enter a subject: ")
    meaning=input("enter its marks ")
    dic[word]=meaning
    print("subject and marks added succsessfully")
    filew=open("dumbdev3.txt","a")
    filew.write(word+":"+meaning+"\n")
  elif userIn==2:
    for i in dic:
      print(i+":"+dic[i])
  
  elif userIn==3:
    print("bye")
    break