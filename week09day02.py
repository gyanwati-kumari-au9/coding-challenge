#Q.https://leetcode.com/problems/longest-increasing-subsequence/submissions/
#TC=O(n^2)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        N = len(nums)
        Dp = [1]*N
        for i in range(N-1):
            for j in range(0,i+1):
                if nums[i+1]>nums[j]:
                    Dp[i+1] = max(Dp[i+1],Dp[j]+1)
        return max(Dp)
        