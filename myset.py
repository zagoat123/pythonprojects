#variable is a storge box that stores a value
#Data Type means a type of data like strings,float,integer,boolean


#Data structure helps you store multiple values
#tuple,list,dictionary

#set
sample_list=[1,1,2,2,3,3,4,4,4,4]
print(set(sample_list))

#set store unique values enclosed in curly brackets

#passwords "@DumbDev3","DevAwsome45"

#Lottery pick
#lucky user=10012


LotteryUser={10001,10003,10005,100012,100016,100056,100078,100090,20001}

if 100012 in LotteryUser:
    print("CONGRATES!!! YOU HAVE WON THE ULTIMATE LOTTERY!!!!")
else:
    print("sorry no lottery for you too bad too sad i win and u dont mu hahaha")


set1=set()
set1.add(3)
set1.add(2)
print(set1)
set1.remove(3)
print(set1)