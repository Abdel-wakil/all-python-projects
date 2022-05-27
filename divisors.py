import os

number=input("enter a number pls :")

num=int(number)

x=range(1,num+1)

s = []

for y in x:
    reste=num%y
    #print(reste)
    if reste==0:
        #print(y)
        s.append(y)
print(s)

print(os.getcwd())