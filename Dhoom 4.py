###   Dhoom 4                   ###
###   Author: Vinod Ranganath   ###
###   Date: 5th, August 2015    ###

import itertools

T = map(int, raw_input().split())
Kvalue = T[0]
Lvalue = T[1]
NK = int(raw_input())
NKvalue = map(int, raw_input().split())
count = 0
merge = 0

def product(List):
    mul=1
    for each in List:
        mul = mul*each
    return(mul)

if Kvalue==Lvalue:
    print("0")
else:
    pass

for l in range (0, (len(NKvalue)+1)):
    for subset in itertools.combinations(NKvalue, l):
        merge = (Kvalue * product(subset))%100000
        if merge==(Lvalue%100000):
            print(len(subset))
            quit()
            
        else:
            pass
        
