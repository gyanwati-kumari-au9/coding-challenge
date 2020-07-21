# Question 1: Given a no n print the sum of numbers from 1 to n. 
# Do it using recursion.
# eg n = 5 sol = 1 + 2 + 3 + 4 + 5

def printSum(n):
    if n<=1:
        return n
    return printSum(n-1)+n

print("-----------------------------------")
print("------Sum of Natural number--------")
print("-----------------------------------") 

if __name__=="__main__":
    n=int(input("Enter any number: "))
    sum=printSum(n)
    print(sum)

# Question 2: Reverse a string using recursion

def revString(str):
    x=len(str)
    if x==0:          #base case
        return
    lastChar=str[x-1]
    print(lastChar,end='')
    revString(str[0:x-1])         # recursion case

print("-----------------------------------")
print("-----------Reverse string-----------")
print("-----------------------------------")

if __name__=="__main__":
    str=str(input("Enter string: "))
    revString(str)