# 1.)Given an array C[], write a program that prints 1 if array is sorted in non-decreasing order, else prints 0.
# Input:
# The first line of input contains an integer T denoting the number of test cases. For each test case there will be two lines. First line contains the size of the array N. Second line contains N space seperated integers of the array C[i].
# Output:
# Print 1 if array is sorted, else print 0.
# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 500
# 1 ≤ C[i] ≤ 1200
# Example:
# Input
# 2
# 5
# 10 20 30 40 50
# 6
# 90 80 100 70 40 30
# Output
# 1
# 0

def isArraySorted(arr,n):
    if len(arr)<2:
        return True
    sort=True
    n=len(arr)
    for i in range (1,n):
        if(arr[i-1]>arr[i]):
            print(arr[i-1],'-',arr[i])
            sort=False
            
    return sort
print("-----------------------------------")
print("-----------check ascending order -----------")
print("-----------------------------------")
if __name__ == "__main__":
    
    testcases=int(input("number of testcases: "))
    for tc in range(0,testcases):
     
        n=int(input("Enter array size: "))
        arr=input("Enter array: ")
        arr=arr.split()
        print(arr)
        for index in range(0,len(arr)):
            arr[index]=int(arr[index])
        if (isArraySorted(arr, n)):
            print("Yes") 
        else:
            print("No") 
     


# 2.)You are given an array A of size N. You need to print elements of A in alternate order.
# Input Format:
# The first line of input contains T denoting the number of testcases. T testcases follow. Each test case contains two lines of input. The first line contains N and the second line contains the elements of the array.
# Output Format:
# For each testcase, print the alternate elements of the array(starting from index 0).
# Your Task:
# Since this is a function problem, you just need to complete the provided function void print(int ar[],int n)
# Constraints:
# 1 <= T <= 200
# 1 <= N <= 105
# 1 <= Ai <= 105
# Example:
# Input:
# 2
# 4
# 1 2 3 4
# 5
# 1 2 3 4 5
# Output:
# 1 3
# 1 3 5
# Explanation:
# Testcase1: print 1, then 3.
# Testcase2: print 1, then 3, then 5.


def stringToArray(strVal):
    # print('Converting',strVal)
    return strVal.split()

def printAlterElements(arr,n):
   
    # print(n,'-',arr)
    res=""
    for i in range(0,n):
        if(i%2 == 0):
            res=res+" "+str(arr[i])
    print("The alternate element of array is: "+ str(res))


print("-----------------------------------")
print("-----------print alternate element-----------")
print("-----------------------------------")
if __name__ == "__main__":
    testcases=int(input("number of testcases: "))
    for tc in range(0,testcases):
        n=input('Enter array size ')
        strInput=str(input('Enter array '))
        # print(n,' - ', strInput)
        x=stringToArray(strInput)
        # print(n,' - ', x)
        printAlterElements(x,int(n))