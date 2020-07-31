class Solution:
    def restoreString(self,s,indices):
        res = [None] * len(s)
        for i, idx in enumerate(indices):
          res[idx] = s[i]
        return ''.join(res)

if __name__=="__main__":
    s=input()
    indices=input()
    x=indices.split()
    for idx in range(0,len(x)):
        x[idx]=int(x[idx])
    sol= Solution()
    print(sol.restoreString(s,x))