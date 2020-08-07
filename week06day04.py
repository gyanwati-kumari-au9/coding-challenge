#Q.1)https://leetcode.com/problems/valid-parentheses/
OPENING_BRACKETS = {"{", "[", "("}
BRACKETS_MAP = {"]": "[", "}": "{", ")": "("}   
class Solution:    
    def isValid(self, s: str) -> bool:
        if not s: 
            return True

        if s[0] not in OPENING_BRACKETS:
            return False 

        stack = Stack()
        for index, bracket in enumerate(s):
            if bracket in OPENING_BRACKETS:
                stack.push(bracket)
            else:
                if stack.empty():
                    return False
                else:
                    last_opening_bracket = stack.pop()
                    if last_opening_bracket != BRACKETS_MAP[bracket]:  
                        return False
        if stack.empty():
            return True
        else:
            return False
        
class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, x):
        self.__stack.append(x)

    def pop(self):
        return self.__stack.pop()
    
    def empty(self):
        return  len(self.__stack)== 0

# Q.2)https://leetcode.com/problems/next-greater-element-ii/
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]    
        for i in range (0,n): 
            val = -1
            for j in range(i+1,n+i):
                k = j % n
                if nums[i]<nums[k]:
                    val=nums[k]
                    break
            res.append(val)
        return res

if __name__=="__main__":
    lst=input()
    lst=lst.split()
    for idx in range(0,len(lst)):
        lst[idx]=int(lst[idx])
    sol=Solution()
    res=sol.nextGreaterElements(lst)
    print(res)
