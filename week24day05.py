# Q. Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element
#  for an element x is the first greater element on the right side of x in array. Elements for which
#   no greater element exist, consider next greater element as -1. Input: [4, 5, 2, 25] 
#   Output: 4 --> 5 5 --> 25 2 --> 25 25 --> -1 Time Complexity Required: O(n) Data structure to use: Stack

def createStack(): 
    stack = [] 
    return stack 


def isEmpty(stack): 
    return len(stack) == 0


def push(stack, x): 
    stack.append(x) 


def pop(stack): 
    if isEmpty(stack): 
        print("Error : stack underflow") 
    else: 
        return stack.pop() 


def printNGE(arr): 
    s = createStack() 
    element = 0
    next = 0
    push(s, arr[0]) 

    for i in range(1, len(arr), 1): 
        next = arr[i] 
        if isEmpty(s) == (False): 
            element = pop(s) 
  
            while element < next : 
                print(str(element)+ " -- " + str(next)) 
                if isEmpty(s) == True : 
                    break
                element = pop(s) 
  
            if  element > next: 
                push(s, element) 
  
        push(s, next) 
  
    while isEmpty(s) == False: 
        element = pop(s) 
        next = -1
        print(str(element) + " -- " + str(next)) 

if __name__ == '__main__': 

    arr = [4, 5, 2, 25] 
    printNGE(arr) 
 