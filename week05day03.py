#1.)https://practice.geeksforgeeks.org/problems/number-of-occurrence/0

def countOccurence(arr,n,x):
    res= 0
    for i in range (0,n):
        if(x==arr[i]):
            res+=1
    if (res==0):
        res= -1
            
    return res

print("-----------------------------------")
print("---------count occurence-----------")
print("-----------------------------------")

if __name__=="__main__":
    testcases=int(input())
    for tc in range(0,testcases):
        y=input()
        y=y.split()
        k=int(y[0])
        z=int(y[1])
        arr=input()
        arr=arr.split()
        for idx in range(0,len(arr)):
            arr[idx]=int(arr[idx])
        
        res=countOccurence(arr,k,z)
        print(res)

# https://leetcode.com/problems/find-peak-element/

def findPeakElement(nums):
    left=0
    right=len(nums)-1
    while(left < right):
        mid=(left+(right-left)//2)
        if(nums[mid] < nums[mid+1]):
            left=mid+1
        else:
            right=mid
    return left

print("-----------------------------------")
print("---------find peak element---------")
print("-----------------------------------")

if __name__=="__main__":
    n=input()
    n=n.split()
    res=findPeakElement(n)
    print(res)
        



