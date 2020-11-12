//Q. Given preorder and inorder traversal of a tree, construct the binary tree.
// Note:
// You may assume that duplicates do not exist in the tree.
// For example, given
// preorder = [3,9,20,15,7]
// inorder = [9,3,15,20,7]
// Return the following binary tree:
// 3
// / \
// 9 20
//     / \
//     15 7


function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
 
/**
* Definition for a binary tree node.
* function TreeNode(val) {
*     this.val = val;
*     this.left = this.right = null;
* }
*/
/**
* @param {number[]} preorder
* @param {number[]} inorder
* @return {TreeNode} 
*/
 
var buildTree = function(preorder, inorder) {
    let preIdx = 0;
    function helper(start, end) {
      if (start >= end) {
        return null;
      }
      let rootIdx = inorder.indexOf(preorder[preIdx]);
      const n = new TreeNode(preorder[preIdx]);
      preIdx++
      n.left = helper(start, rootIdx);
      n.right = helper(rootIdx + 1, end);
      return n;
    }
    return helper(0, preorder.length);
      
  };
rt = [3,9,20,15,7]
rot=[9,3,15,20,7]
console.log("Tree :",buildTree(rt,rot));