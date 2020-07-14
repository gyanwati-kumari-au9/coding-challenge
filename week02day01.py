# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.
# Example 2:

# Input: date = "2019-02-10"
# Output: 41
# Example 3:

# Input: date = "2003-03-01"
# Output: 60
# Example 4:

# Input: date = "2004-03-01"
# Output: 61
 

# Constraints:

# date.length == 10
# date[4] == date[7] == '-', and all other date[i]'s are digits
# date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.


def number_of_days(string_date):
    d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    date=string_date.split("-")
    day=int(date[2])
    month=date[1]
    year=int(date[0])

    leap=False
    if(year%4==0 or year%100==0 or year%400==0):
        print("year is a leap year: ",year)
        leap = True
    for mon in range(1,int(month)):
        if (mon==2 and leap):
            day+=29
        else:
            day+=d[mon]
    print(day)
date=str(input("Enter the date in format yyyy-mm-dd: "))
number_of_days(date)


# 2.)Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
#(solve it without type casting)



def strToList(strVal):
    lst = []
    x=len(strVal)
    for l1 in range (0,x):
        lst.append(int(strVal[l1]))
    return lst

def sumString(num1,num2):
    x=strToList(num1)
    y=strToList(num2)
    k=max(len(x), len(y))+1
    
    z=0
    a=len(x)
    b=len(y)
    sum=[]
    for i in range(0,k):
        index=k-i
        
        if (i < a):
            z=z+x[a-i-1]
        if(i<b):
            z=z+y[b-i-1]
        sum.append(z%10)
        z=int(z/10)
        
    retVal=""
    for dig in sum[::-1]:
        retVal+=str(dig)
    return str(int(retVal))


num1=input("Enter number of first string: ")
num2=input("Enter number of second string: ")
z=sumString(num1,num2)

print(z)