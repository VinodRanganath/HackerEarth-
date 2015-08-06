### Panda and XOR           ###
### Author: Vinod Ranganath ###
### Date: 4th, August 2015  ###


import itertools

n = int(raw_input()) #Get user input for no. of values
N = [] #Initialize values list
MAXOR = 0 #Initialize MAXOR variable
combarray = [] #Initialize combarray list (for storing the list of combinations)
XORcomb = [] #Initialize XORcomb list (for storing XOR of all combinations)
index = [] #Initialize index list (to store indices of repeated XOR results)
finalcomb = [] #List to store the combinations with equal XOR results
finalcount = []
XOR = 0

#Get user input for values and store in array N
for i in range (n):
    N1 = int(raw_input())
    N.append(N1)

#Get the various non-repetitive combinations of values in the array
#and compute XOR for each combination and store in XORcomb list
for l in range (0, (len(N)+1)):
    for subset in itertools.combinations(N, l):
        combarray.append(subset)
        if len(subset)>1:
            for s in subset:
                XOR = XOR^int(s)
        elif len(subset)==1:
            XOR = int(subset[0])^0
        XORcomb.append(XOR)
        XOR=0

#Function to acquire indices of repeated results
def duplicates(lst, item):
    return [j for j, x in enumerate(lst) if x == item]

#Display Combinations with equal results
for each in N:
    dups = duplicates(XORcomb, each)
    #print(dups)
    for index in range (0, len(dups)):        
        finalcomb.append(combarray[dups[index]])
    print("Combinations with XOR result of %r: %r" %(XORcomb[dups[index]], finalcomb))
    if len(finalcomb)>1:
        finalcount.append(len(finalcomb))
    del finalcomb[:]
print(len(finalcount))
