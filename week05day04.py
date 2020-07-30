#Q1. https://leetcode.com/problems/two-sum/ Solve it in O(n2) O(nlogn), O(n)

def twoSum(nums,target):
    for i in range (len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i]+nums[j]==target):
                print(i,j)
                return True
    return False

print("-----------------------------------")
print("---------Two sum For O(n^2)---------")
print("-----------------------------------")  

if __name__=="__main__":
    n=input()
    n=n.split()
    for idx in range(0,len(n)):
        n[idx]=int(n[idx])
    k=int(input())
    res=twoSum(n,k)
    print(res)

#Note:-There are two nested loops 
# loop first iteration going in n times & loop second depend on the variable.
# Therefore time complexitity = O(n^2).
# if condition ------time complexity is constant
# space complexity-------O(1)


# how sum of time complexity O(nlogn) is possible



def twoSum(nums,target):
    d={}
    for i ,num in enumerate(nums):
        if (target - num in d) :
            print(d[target - num],i)
            return True
        d[num]=i
    return False

print("-----------------------------------")
print("---------Two sum For O(n)---------")
print("-----------------------------------")  

if __name__=="__main__":
    n=input()
    n=n.split()
    for idx in range(0,len(n)):
        n[idx]=int(n[idx])
    k=int(input())
    res=twoSum(n,k)
    print(res)

# Note:- here we have one loop so iteration going in n times
#  if conditions ----time complexity is constant
# Therfore, time complexity = O(n)


