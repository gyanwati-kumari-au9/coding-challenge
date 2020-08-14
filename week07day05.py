#Q.1)https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        anslist=[]
        if root is None:
            return anslist
        q = []
        q.append(root)
        while (len(q) != 0):
            size = len(q)
            list = []
            while size != 0:
                temp =q.pop(0)
                list.append(temp.val)
                if temp.left is not None:
                    q.append(temp.left)
                    
                if temp.right is not None:
                    q.append(temp.right)
                size -= 1
            anslist.append(list)
        return anslist