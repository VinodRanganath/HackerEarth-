###   Prom Night                ###
###   Author: Vinod Ranganath   ###
###   Date: 3rd, August 2015    ###


T = int(input("Enter no. of test cases: ")) #Get no of test cases
result = []

#Match making function 
def match(M, N, bheight, gheight):
    count = 0
    mod = 0
    maximum = 0
    if M<=N:
        for i in range (0, M):
            if len(gheight)!=0:
                for j in range (0, len(gheight)):
                    if bheight[i]>gheight[j]:
                        num_array.append(gheight[j])
                    else:
                        pass
                if len(num_array)!=0:
                    maximum = max(num_array)
                    del num_array[:]
                    gheight.remove(int(maximum))
                    count += 1
        return count

for t in range (1, T+1):
    n = input("Enter no. of boys and girls respectively: ")
    M = int(n[0])  #No. of boys
    N = int(n[2])  #No. of girls
    height1 = []
    height2 = []
    bheight = []
    gheight = []
    num_array = []

    #Get user input for values and store in array bheight
    height1 = input()
    bheight.append(int(height1.split())
    
    #Get user input for values and store in array gheight
    height2 = input()
    gheight.append(int(height2.split())

    c = match(M, N, bheight, gheight) #Call match-making function and return value to c

    #Success condition --> no. of paired boys = total no. of boys 
    if c == M:
        result.append("YES")
    else:
        result.append("NO")

#Print result of test cases(in order)
for each in result:
    print("%s" %each)
