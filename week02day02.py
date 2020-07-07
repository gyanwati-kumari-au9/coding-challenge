# Q1.
# Write a program that takes input from the user as marks in 5 subjects and assigns a grade according to the following rules:
# Perc = (s1+s2+s3+s4+s5)/5.
# A, if Perc is 90 or more B, if Perc is between 70 and 90(not equal to 90) C, if Perc is between 50 and 70(not equal to 90) D, if Perc is between 30 and 50(not equal to 90) E, if Perc is less than 30

s1=int(input("enter marks of the 1st subject:"))
s2=int(input("enter marks of the 2nd subject:"))
s3=int(input("enter marks of the 3rd subject:"))
s4=int(input("enter marks of the 4th subject:"))
s5=int(input("enter marks of the 5th subject:"))

avg=(s1+s2+s3+s4+s5/5)

if (avg>=90) :
    print("Grade: A ")
elif (avg<=70 and avg<90) :
    print("Grade: B ")
elif (avg<=50 and avg<70) :
    print("Grade: C ")
elif (avg<=30 and avg<50) :
    print("Grade: D ")
elif (avg<30) :
    print("Grade: B ")
else :
    print("Fail")