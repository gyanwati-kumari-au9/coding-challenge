# Given a sorted array arr[] of N integers and a number K is given. The task is to check 
# if the element K is present in the array or not.
# Input:
# First line of input contains number of testcases T. For each testcase, 
# first line of input contains number of elements in the array and the 
# number K seperated by space. Next line contains N elements.
# Output:
# For each testcase, if the element is present in the array print "1" (without quotes), else print "-1" (without quotes).
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 106
# 1 <= K <= 106
# 1 <= arr[i] <= 106
# Example:
# Input:
# 2
# 5 6
# 1 2 3 4 6
# 5 2
# 1 3 4 5 6
# Output:
# 1
# -1
# Explanation:
# Testcase 1: Since, 6 is present in the array at index 4 (0-based indexing), so output is 1.
# Testcase 2: Since, 2 is not present in the array, so output is -1.

print("-----------------------------------")
print("--check given element are present or not--")
print("-----------------------------------")

if __name__=="__main__":
    testcases=int(input("Enter number of testcases: "))
    for tc in range(0,testcases):
        N=input("enter size of array and checking element:")
        y=N.split()
        N=y[0]
        k=y[1]
        x=input("Enter sorted array of element: ")
        x=x.split()
        presentVal=-1
        for i in range(0,len(x)):
            if(x[i]==k):
                presentVal=1
                break
        print(presentVal)


# Q2. Write a program which takes two integers n and m and compute (n^m) n to the power m.
# Try to use recursion do Q2.

def pow(n,m):
    if(m==0):
        return 1
    return n*pow(n,m-1)

print("-----------------------------------")
print("------print value of n**m----------")
print("-----------------------------------")

n=int(input("Enter any number:"))
m=int(input("Enter any number:"))
result=pow(n,m)
print(result)