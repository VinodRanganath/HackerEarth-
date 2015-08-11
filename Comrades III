### Comrades III            ###
### Author: Vinod Ranganath ###
### Date: 11th, August 2015 ###

N = int(raw_input())
H = map(int, raw_input().split())
T = int(raw_input())
wake_list = []
sleep_list = []
S = []
c = 0
result = 0
soldiers = []

#Find commander
if H[0]!=0:
    for i,each in enumerate(H):
        if each==0:
            c=H[i-1]
            H.remove(each)
        else:
            pass

#Find soldiers
for j in range (1,N+1):
    if j not in H:
        S.append(j)
        soldiers.append(j)

#Establish heirarchy
if c!=0:
    H.remove(c)
    for every in H:
        S.append(every)
    S.append(c)

#Execute process for given number of orders
for t in range (0,T):        
    order = map(int, raw_input().split())
    if t==0:
        wake_list=soldiers #All soldiers awake initially
    else:
        pass

    #Order1-->Wake up
    if order[0]==1:
        for w in S:
            if S.index(w)<S.index(order[1]):
                if w not in wake_list:
                    wake_list.append(w)
                else:
                    continue
            else:
                continue

    #Order2-->Sleep
    if order[0]==2:
        for s in S:
            if S.index(s)<S.index(order[1]):
                sleep_list.append(s)
                wake_list.remove(s)
            else:
                continue

    #Order3-->Display no. of soldiers awake
    if order[0]==3:
        for p in S:
            if S.index(p)<S.index(order[1]):
                result=len(wake_list)
            else:
                continue
        print(result)
