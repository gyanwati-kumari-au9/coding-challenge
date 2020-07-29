# Q1. Implement merge sort on your own and analyze its time complexity.
     #same as question no. 2
    #  time complexity= O(nlog(n1+n2))

# Q2.https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays/0

def mergeArrays(arr1, arr2, n1, n2): 
    arr3 = [None] * (n1 + n2) 
    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2: 
        if arr1[i] < arr2[j]: 
            arr3[k] = arr1[i] 
            k = k + 1
            i = i + 1
        else: 
            arr3[k] = arr2[j] 
            k = k + 1
            j = j + 1
    while i < n1: 
        arr3[k] = arr1[i] 
        k = k + 1
        i = i + 1
    while j < n2: 
        arr3[k] = arr2[j] 
        k = k + 1
        j = j + 1
    print("Array after merging") 
    
    for i in range(n1 + n2): 
        print(str(arr3[i]), end = " ") 
    
print("-----------------------------------")
print("---------print merge array---------")
print("-----------------------------------")

if __name__=="__main__":
    testcases=int(input())
    for tc in range(0,testcases):
        sz=input()
        sz=sz.split()
        n1=int(sz[0])
        n2=int(sz[1])
        x=input()
        y=input()
       
        x=x.split()
        for index in range(0,len(x)):
            x[index]=int(x[index])
        x.sort()
        y=y.split()
        for index in range(0,len(y)):
            y[index]=int(y[index])
        y.sort()

        mergeArrays(x,y,n1,n2)
        
    print()

# Q3. https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0

def sort012( a, arr_size): 
    left = 0
    right = arr_size - 1
    mid = 0
    while mid <= right: 
        if a[mid] == 0: 
            a[left], a[mid] = a[mid], a[left] 
            left = left + 1
            mid = mid + 1
        elif a[mid] == 1: 
            mid = mid + 1
        else: 
            a[mid], a[right] = a[right], a[mid]  
            right = right - 1
    return a  

print("-----------------------------------")
print("---------print Sorted 0s,1s,2s------")
print("-----------------------------------")

if __name__=="__main__":

    testcases=int(input())
    for tc in range(0,testcases):
        n=int(input())
        y=input()
        y=y.split()
        for idx in range(0,len(y)):
            y[idx]=int(y[idx])
        y.sort()
        res=sort012( y,n)
        rstr=""
        for i in range(len(res)):
            if rstr=="":
                rstr=str(res[i])
            else:
                rstr+=" "+str(res[i])
        
        print(rstr)