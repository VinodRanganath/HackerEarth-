### Rasta and Darie         ###
### Author: Vinod Ranganath ###
### Date: 18th, August 2015 ###

t = int(raw_input())
numbers = []
final_list = []
result = []

#Compute for all test cases
for every in range (0, t):
    n, p, k = map(int, raw_input().split()) #Get size, step and target respectively
    #List form 1 to n
    for i in range (1,n+1):
        numbers.append(i)
    final_list.append(1) #Set initial step at 1
    process = True
    count = 0 #Initialize count
    while process:
        count+=p #Count in steps of p(user input)
        #Wrap around list and count in clockwise direction
        if numbers[count%n]!=1:
            final_list.append(numbers[count%n]) #Get value at each step(p) until initial position
        else:
            final_list.append(1)
            process=False
    final_list=sorted(final_list) #Sort step results in ascending order
    if len(final_list)>k:
        result.append(final_list[k])
    else:
        result.append(-1)
    del final_list[:]
    del numbers[:]

#Print results
for each in result:
    print(each)
