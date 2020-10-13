// Given a binary tree, find its maximum depth.
// The maximum depth is the number of nodes along the longest path from the root node
// down to the farthest leaf node.
// Note: A leaf is a node with no children.
// Example:
// Given binary tree [3,9,20,null,null,15,7],
//  3
//  / \
//  9 20
//  / \
//  15 7
// return its depth = 3

function TreeNode(val) {
       this.val = val;
       this.left = this.right = null;
    }
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    return maxDepthHandler(root,1)
     
 };
 var maxDepthHandler = function(root, num){
    if(root == null){
        return 0
    }
   if (root.right == null && root.left == null){
       return num+1
   }
   if (root.right && root.left){
       return Math.max( maxDepthHandler(root.right, num+1), maxDepthHandler(root.left, num + 1))
   }  else if (root.right != null){
       return maxDepthHandler(root.right, num+1)
   } else {
       return maxDepthHandler(root.left, num+1)
   }
 };

root = new TreeNode(3);
root.left = new TreeNode(9);
root.right = new TreeNode(20);
root.left = new TreeNode(null);
root.right = new TreeNode(null);
root.left = new TreeNode(15);
root.right = new TreeNode(7);
console.log("max-depth :" ,maxDepth(root));