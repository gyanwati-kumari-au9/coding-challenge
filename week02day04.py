# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i^2. See the sample for details.
# Input Format
# The first and only line contains the integer, n.
# Constraints
# 1<=n<=20
# Output Format
# Print  lines, one corresponding to each i. 
    
n=int(input("enter any number : "))
i=0
for x in range(0,n,):
    print(i*i) 
    i=i+1




#Q2. Print the below pattern given n by user
        #       *
        #     *   *
        #    *  *  *
        #   *  *  *  *


n=int(input("enter any number: "))

x=2*n-1


for row in range (1,n+1) :
    numstart=0
    startposition=n-row+1
    for column in range(1,x+1) :
        # print("==>",column, row, startposition, numstart, x)
        if (column>startposition) :
            if(numstart>=row) :
            break
            numstart=numstart+1
            # print("=IN=>",column, row, startposition, numstart, x)
            print("* ",end="")
            print("  ",end="")
        else :
            print("  ", end='')
    print("\r")
           



