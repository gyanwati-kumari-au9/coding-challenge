# Q1. Write and practice all the 4 sorting algorithms
# Bubble
# Optimized Bubble
# Insertion
# Selection

# Answer:-
# 1.)Bubble sort algorithms:- It is a simple comparison-based sorting algorithms that works by repeatally 
# swapping the adjacent elements if they are not in order.
# [5,3,8,6,7,2]
# first compare the two elements
# iteration 1
# if 5>3 -------True-----is swapping
# [3,5,8,6,7,2]
# if 5>8 -------False-----no swapping
# [3,5,8,6,7,2]
# if 8>6----------True-----is swapping
# [3,5,6,8,7,2]
# if 8>7--------True------is swapping
# [3,5,6,7,8,2]
# if 8>2--------True-----is swapping
# [3,5,6,7,2,8]
# iteration 2 (and continue comparing each pair)
# iteration 3 (and continue comparing each pair)
# iteration 4 (and continue comparing each pair)
# iteration 5 (and continue comparing each pair)
# swapping is done
# [2,3,5,6,7,8]

def sort(n):
    for i in range(len(n)-1,0,-1):
        for j in range(i):
            if (n[j]>n[j+1]):
                temp=n[j]
                n[j]=n[j+1]
                n[j+1]=temp
    return n
print("-----------------------------------")
print("-----------Bubble sort-----------")
print("-----------------------------------")
n=input("Enter the list elements in unsorted order: ")
n=n.split()
x=sort(n)
print(x)

# 2.) Optimized bubble sort algorithms:-by default 

def optimizedBubbleSort(lst):
    sorted=True
    n=len(lst)
    while(sorted==True and n>1):
        sorted=False
        for i in range(n-1):
            if(lst[i]>lst[i+1]):
                lst[i],lst[i+1]=lst[i+1],lst[i]
                sorted=True
        n-=1
    return lst
print("-----------------------------------")
print("-----------optimized bubble sort -----------")
print("-----------------------------------")
x=input("Enter list of elements in unsorted order: ")
x=x.split()
y=optimizedBubbleSort(x)
print(y)
# 3.) Insertion sort algorithms:-It is a simple sorting algorithms,that builds the final 
# sorted list one item at a time.
# [3,2,5,7,4]
# sorted                unsorted
# 3                      2 5 7 4
# iteration 1 (first move to sorted side and compare two elements)
# 3 2                    5 7 4
# if 3>2------yes 
# 2 3                    5 7 4
# iteration 2
# 2 3 5                  7 4
# if 3>5--------No
# iteration 3
# 2 3 5 7                 4
# if 5>7-------No
# iteration 4
# 2 3 5 7 4
# if 7>4-----yes
# 2 3 5 4 7 
# now compare to each element and switch to elements in ascending order.
# 2 3 4 5 7
def insertionSort(lst):
    n=len(lst)
    
    for i in range(1,n):
        valueToSort=lst[i]
        j=i-1
        while(j>=0 and valueToSort<lst[j]):
            lst[j+1]=lst[j]
            j=j-1
            lst[j+1]=valueToSort
    return lst
print("-----------------------------------")
print("-----------Insertion sort -----------")
print("-----------------------------------")        
x=input("Enter list of elements in unsorted order: ")
x=x.split()
y=insertionSort(x)
print(y)

# 4.) Selection sort algorithms:- 
# > search the list and find out the minimum value
# > swap minimum(maximum) number with first element.
# > take the sublist(ignore sorted part) and repeat step1 and 2 untill all the elements are sorted.
# [4,6,2,8,7]------unsorted
# iteration 1 first search minimum value and compare to each element
# sorted               unsorted
# 2                     6 4 8 7
# iteration 2
# 2 4                   6 8 7
# iteration 3
# 2 4 6                   8 7
# iteration 4
# 2 4 6 7 8

def selectionSort(lst):
    for i in range(len(lst)):
        minValue= i
        for j in range(i+1, len(lst)):
            if lst[minValue] > lst[j]:
                minValue = j
                #swap
        lst[i], lst[minValue] = lst[minValue], lst[i]
    return lst
    
print("-----------------------------------")
print("-----------selection sort -----------")
print("-----------------------------------")

n=input("Enter list of elements in unsorted order : ")
n=n.split()
x=selectionSort(n)
print(x)


# 2.)Given a list of scores of different students, return the average score of each student's top five scores in 
# the order of each student's id.
# Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score. 
# The average score is calculated using integer division.
# Example 1:
# Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# Explanation: 
# The average of the student with id = 1 is 87.
# The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.

# Function to compute average of Integer list
def avg(arr):
    sum=0
    for i in range(0,len(arr)):
        sum+=arr[i]
    
    return sum/len(arr)

# Function to sort dicitionary keys based on value
def sortDict(d):

    # for i in range(len(d)-1,0,-1):
    #     for j in range(i):
    #         if d[j]>d[j+1]:
    #             temp=d[j]
    #             d[j]=d[j+1]
    #             d[j+1]=temp
    return sorted(d.items(), key=lambda x: x[1], reverse=True)
print("-----------------------------------")
print("----Avg marks of top five students-----")
print("-----------------------------------")
# Main function
if __name__=="__main__":
    x = input()
    d1 = x.split(',')
    for index in range (0, len(d1)):
        d1[index] = d1[index].split()
    d2={}
    for index,value in d1:
        if(index not in d2 ):
            d2[index]=[int(value)]
        else:
            d2[index].append(int(value))
    for index,value in d2.items():
        # print(index,value)
        d2[index]=round(avg(value))
    sortedResult = sortDict(d2)
    print(sortedResult[0:5])