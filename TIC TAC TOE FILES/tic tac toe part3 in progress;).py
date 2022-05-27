
EBG= [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]
for h0 in EBG:
    print("        ",h0)
P1=[]
P2=[]
i=1
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
            for h in EBG:
                print("        ",h)
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
            for h1 in EBG:
                print("        ",h1)
            break
    

        
    