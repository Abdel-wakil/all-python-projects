l=["a","r","t","r"]

j=[""," "," "," ",]

letter=input("enter guess: ")

index=-1

l_index=[]

for i in l:
    index+=1
    if i==letter:
        l_index+=[index]
#print(l_index)
for u in range(len(l_index)):
    j[l_index[-1]]=letter
    l_index.pop(-1)

print(j)