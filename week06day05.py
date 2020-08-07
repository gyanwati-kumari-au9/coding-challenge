# Q.1)https://leetcode.com/problems/min-stack/
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = []  
    def is_empty(self):
        return  len(self.__stack)== 0

    def push(self, x: int) -> None:
         self.__stack.append(x)   

    def pop(self) -> None:
         return self.__stack.pop()
        
    def top(self) -> int:
        return self.__stack[-1]
    
    def getMin(self) -> int:
        min=self.__stack[0]
        for i in range(1,len(self.__stack)):
            if min > self.__stack[i]:
                min=self.__stack[i]
        
        return min
          
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()