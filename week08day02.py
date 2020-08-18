#Q1. https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    return (i,j)

# Q2. https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if(root.val == sum and (root.left == None and root.right == None)):
            return True
        return self.hasPathSum(root.left,sum-root.val)or self.hasPathSum(root.right,sum-root.val)