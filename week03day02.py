# Q1. Write a Python program to create a dictionary from a string. Note: Track the count
# of the letters from the string. Sample string : 'w3resource' Expected output: {'3': 1, 's': 1,
# 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

def createDictionary(sample_str):
    d={}
    for letter in sample_str:
        d[letter]=d.get(letter,0)+1
    return d
x=input("Enter input:")
d=createDictionary(x)
print(d)


# 2.)Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.



def strToDict(str1):
    d1={}
    for letter in str1:
        d1[letter]=d1.get(letter,0)+1
    return d1


def check_anagram(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    d1=strToDict(str1)
    d2=strToDict(str2)

    if(sorted(d1)==sorted(d2)):
        return True
    else:
        return False
a=input("Enter input1: ")
b=input("Enter input2: ")
x=check_anagram(a,b)
print(x)



# Q3. Write a Python script to generate and print a dictionary that contains a number
# (between 1 and n) in the form (x, x*x).

def dict(n):
    d={}
    for x in range(1,n+1):
        d[x]=x*x
    return d
        
num= int(input("Enter any number: "))
d=dict(num)
print(d)