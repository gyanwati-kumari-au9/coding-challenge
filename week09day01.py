#https://www.geeksforgeeks.org/maximum-profit-sale-wines/
#Question 1: Solve the wine dp problem.
dp=[[]]
def maxProfit(P,start, end,n, year):

    if (start > end):
        return 0
    elif (dp[start][end] != None):
        return dp[start][end]
    else:
        dp[start][end] = max(P[start] * year + maxProfit(P, start + 1, end, n, year + 1), P[end] * year + maxProfit(P, start, end - 1, n, year + 1))
        return dp[start][end]
    

if __name__=="__main__":
    w=int(input())
    p=input()
    p=p.split()
    for idx in range(len(p)):
        p[idx]=int(p[idx])
    dp=[[None for i in range(w)] for i in range (w)] # create empty array
            
    res=maxProfit(p,0,w-1,w,1)
    print(res)