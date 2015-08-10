### ICPC Team Management    ###
### Author: Vinod Ranganath ###
### Date: 6st, August 2015  ###

import random

T = int(raw_input())
namelist = []
name_length = []
index_list = []
t = []
result = []
N1 = []

def duplicates(lst, item):
    return [j for j, x in enumerate(lst) if x == item]

for j in range (0, T):
    count=0
    N, K = map(int, raw_input().split())
    for i in range (0,N):
        name = str(raw_input())
        namelist.append(name)
    for each in namelist:
        name_length.append(len(each))
    del t[:]
    t = list(set(name_length))
    for every in range (0, len(t)):
        index_list.append(duplicates(name_length,t[every]))
    
    for each in index_list:
        print(each)
        #N1.append(random.sample(set(each),K))
    if len(N1)==N or K==1:
        result.append("Possible")
    else:
        result.append("Not possible")
    del N1[:]
    del index_list[:]
    del t[:]
    del name_length[:]
    del namelist[:]

for r in result:
    print(r)
