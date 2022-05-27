BG= [[1, 1, 2],
     [2, 2, 1],
     [1, 1, 2]]

v=[]
j2=0
for u in range(3):
    j=0
    eq=BG[u][0]
    for i in range(3):
        if eq==BG[u][i]:
            j+=1
    if j==3:
        if eq==1:
            print("P1 wins hahaha")
            j2+=1
        elif eq==2:
            print("P2 wins hahaha")
            j2+=1
            
#print(BG)

for z in range(3):
    v=[]
    v+=[BG[0][z]]
    v+=[BG[1][z]]
    v+=[BG[2][z]]
    eq1=v[0]
    j1=0
    for i1 in range(3):
        if eq1==v[i1]:
            j1+=1
    if j1==3:
        if eq1==1:
            print("P1 wins hahaha")
            j2+=1
        elif eq1==2:
            print("P2 wins hahaha")
            j2+=1

if BG[0][0]==BG[1][1]==BG[2][2]:
    if BG[0][0]==1:
        print("P1 wins hahaha")
        j2+=1
elif BG[2][0]==BG[1][1]==BG[0][2]:
    if BG[2][0]==2:
        print("P2 wins hahaha")
        j2+=1
if j2==0:
    print("draaaw")

    

