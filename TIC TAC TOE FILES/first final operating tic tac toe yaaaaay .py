
def winning_algo(game):
    global j2
    global j6
    j6=0
    v=[]
    j2=0
    for u in range(3):
        j=0
        eq=game[u][0]
        for i in range(3):
            if eq==game[u][i]:
                j+=1
        if j==3:
            if eq==1:
                print("P1 wins hahaha")
                j2+=1
            elif eq==2:
                print("P2 wins hahaha")
                j2+=1
    for z in range(3):
        v=[]
        v+=[game[0][z]]
        v+=[game[1][z]]
        v+=[game[2][z]]
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
    if game[0][0]==game[1][1]==game[2][2]:
        if game[0][0]==1:
            print("P1 wins hahaha")
            j2+=1
    elif game[2][0]==game[1][1]==game[0][2]:
        if game[2][0]==2:
            print("P2 wins hahaha")
            j2+=1
    j9=0      
    for h10 in game:
        if 0 not in h10:
            j9+=1
    if j9==3:
        if j2==0:
            print("draaaw")
            j6+=1
            
            
###########winning_algo##############



EBG= [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]
for h0 in EBG:
    print("        ",h0)
P1=[]
P2=[]
i=1
n3=0
while i!=0:
    while i!=0:
        u=input("enter coordonate P1: ")
        P1=u.split(",")
        P1_0=int(P1[0])
        P1_1=int(P1[1])
        if EBG[P1_0-1][P1_1-1]!=0:
            print("choose an empty slot plz ;) ")
        else:
            EBG[P1_0-1][P1_1-1]=1
            n3+=1
            for h in EBG:
                print("        ",h)
            break
    if n3>=5:
        winning_algo(EBG)
        if j2==1 or j6==1:
            break
    
    while i!=0:
        j=input("enter coordonate P2: ")
        P2=j.split(",")
        P2_0=int(P2[0])
        P2_1=int(P2[1])
        if EBG[P2_0-1][P2_1-1]!=0:
            print("choose an empty slot plz ;) ")
        else:
            EBG[P2_0-1][P2_1-1]=2
            n3+=1
            for h1 in EBG:
                print("        ",h1)
            break