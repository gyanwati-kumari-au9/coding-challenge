#Q1. https://leetcode.com/problems/unique-paths/

def findNoOfWays(m,n):
    #print('calculating for',m , n)
    if (m ==1 or n==1):
        if(m==1 and n==1):
            return 0
        else:
            return 1
    else:
        return (findNoOfWays(m,n-1)+findNoOfWays(m-1,n))

print("-----------------------------------")
print("-------Find Number of Path-----------")
print("-----------------------------------")

if __name__=="__main__":
    m=int(input("Enter number of columns: "))
    n=int(input("Enter number of rows"))
    res=findNoOfWays(m,n)
    print(res)

# Q2. Find the substrings of a string
# Eg “abc” - {“”, “a”, “ab”, “abc”, “b”, “bc”, “abc”}
# Try to do Q2. with recursion also

def lst_substrings(s):
    lst = [s]
    if len(s) > 0:
        lst.extend(lst_substrings(s[1:]))
        lst.extend(lst_substrings(s[:-1]))
    return list(set(lst))

print("-----------------------------------")
print("---------Find all substring----------")
print("-----------------------------------")

if __name__=="__main__":
    str1=str(input("Enter any string: "))
    sub = lst_substrings(str1)
    sub.sort(key=lambda item: (-len(item), item))
    print(sub)


