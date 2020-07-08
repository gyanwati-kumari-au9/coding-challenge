# The included code stub will read an integer, , from STDIN.

# Without using any string methods, try to print the following:
#123...n

# Note that "" represents the consecutive values in between.

# Example n=5

# Print the string 12345.

# Input Format

# The first line contains an integer n.

# Constraints

# 1<=n<=150
# Output Format

# Print the list of integers from 1 through n as a string, without spaces.

n=int(input("Enter any numbers : "))
x=1

while (x<=n) :
    print(x , end = '') 
    x=x+1


# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i^2. See the sample for details.
# Input Format
# The first and only line contains the integer, n.
# Constraints
# 1<=n<=20
# Output Format
# Print  lines, one corresponding to each i. 
    
n=int(input("enter any number : "))
i=0

while (i<n) :
    print(i*i) 
    i=i+1



# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  a//b. The second line should contain the result of float division,  a/b .
# No rounding or formatting is necessary.
# Input Format
# The first line contains the first integer,a.
# The second line contains the second integer,b .
# Output Format
# Print the two lines as described above.


a=int(input("enter any  numbers : "))
b=int(input("enter any numbers : "))
c=a//b
d=a/b
print("floor division of a and b is: ",int(c))
print("division of a and b is: ",float(d))


# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Input Format
# The first line contains the first integer, a.
# The second line contains the second integer,b .
# Constraints
# 1<=a<=10^10
# Output Format
# Print the three lines as explained above

a=int(input("enter any  numbers : "))
b=int(input("enter any numbers : "))
x=a+b
y=a-b
z=a*b

print("addition of a and b is: ",float(x))
print("difference of a and b is: ",float(y))
print("multiplication of a and b is: ",float(z))
