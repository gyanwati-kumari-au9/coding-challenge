#1.) https://practice.geeksforgeeks.org/problems/subsets/0
print("-----------------------------------")
print("---------print Subset--------------")
print("-----------------------------------")
if __name__=="__main__":
    testcases=int(input())
    for tc in range(0,testcases):

        n =int(input())
        x=input()
        x=x.split()
        uniq=[]
        for i in range(2**n):
            subset = ""
            for j in range(0,n):
                if i & (1 << j) !=0:
                    if(subset==""):
                        subset = str(x[j])
                    else:
                        subset+=" "+str(x[j])
            
            subset="("+subset+")"
            if (subset not in uniq):
                uniq.append(subset)
                print(subset, end="")
    print()

#2.)https://practice.geeksforgeeks.org/problems/combination-sum/0

def formatArray(lst):
    res="("
    for val in lst:
        res+=" "+str(val)
    
    res+=")"
    return res

def combinationSum(lst, target, idx, curr, res):
    if target == 0: 
        res.append(formatArray(curr[:]))
        return
    
    for i in range(idx, len(lst)):
        if lst[i] > target: 
            return
        curr.append(lst[i])
        combinationSum(lst, target - lst[i], i, curr, res)
        curr.pop()
    return res
   
print("-----------------------------------")
print("---------print combinationSum--------------")
print("-----------------------------------")

if __name__ == '__main__': 
    testcases=int(input())
    for tc in range(0,testcases):
        n=int(input())
        x=input()
        x=x.split()
        y=int(input())
        
        for index in range(0,len(x)):
            x[index]=int(x[index])
        x.sort()
        res=formatArray(combinationSum(x,y,0,[],[]))
        print(res)
    print()

