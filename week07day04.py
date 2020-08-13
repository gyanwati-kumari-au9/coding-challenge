#Q.1)https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
def countLeaves(root):
    # Code here
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
        
    leftans = countLeaves(root.left)
    rightans = countLeaves(root.right)
    return leftans+rightans

#Q.2)https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''        
# return the Height of the given Binary Tree
def height(root):
    # code here
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    
    return max(height(root.left),height(root.right))+1

#Q.3)https://leetcode.com/problems/binary-tree-paths/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findRootToLeafPaths(self,root,curPath,allPaths):
        if root is None:
            return
        if root.left is None and root.right is None:
            curPath.append(str(root.val))
            allPaths.append(curPath[:])
            curPath.pop()
            
        curPath.append(str(root.val))
        self.findRootToLeafPaths(root.left,curPath,allPaths)
        self.findRootToLeafPaths(root.right,curPath,allPaths)
        curPath.pop()
        
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        allPaths=list()
        self.findRootToLeafPaths(root,[],allPaths)
        res = list()
        for path in allPaths:
            res.append("->".join(path))
        return res
        