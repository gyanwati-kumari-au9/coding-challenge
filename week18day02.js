// Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the
// given sum.
// Note: A leaf is a node with no children.
// Example:
// Given the below binary tree and sum = 22,
//  5
//  / \
//  4 8
//  / / \
//  11 13 4
// / \ / \
// 7 2 5 1
// Return:
// [
//  [5,4,11,2],
//  [5,8,4,5]
// ]

function TreeNode(val, left, right) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {number[][]}
 */
var pathSum = function(root, sum) {
    var res = [];
    getSum(root, sum, [], res);
    return res;
    
};
var getSum = function (root, sum, now, res) {
  if (!root) return;

  now.push(root.val);

  if (root.val === sum && !root.left && !root.right) res.push(now);

  getSum(root.left, sum - root.val, Array.from(now), res);
  getSum(root.right, sum - root.val, Array.from(now), res);
};

var arr = [5,4,8,11,null,13,4,7,2,null,null,5,1],
    tree;

function insertBinTree (t = {value: void 0, left: void 0, right: void 0}, n){
  t.value !== void 0 ? t.value > n ? t.left = insertBinTree(t.left,n)
                                   : t.right = insertBinTree(t.right,n)
                     : t.value = n;
  return t;
}

tree = arr.reduce(insertBinTree, void 0);
// rt = new TreeNode(5);
// rt.left = new TreeNode(4);
// rt.right = new TreeNode(8);
// rt.left.left = new TreeNode(11);
// rt.left.right = new TreeNode(null);
// rt.left.right.left = new TreeNode(13);
// rt.left.right.right = new TreeNode(4);
// rt.left.left.left= new TreeNode(7);
// rt.left.left.right = new TreeNode(2);
// rt.left.right.left = new TreeNode(null);
// rt.left.right.right = new TreeNode(null);
// rt.left.left.right.left = new TreeNode(5);
// rt.left.left.right.right = new TreeNode(1);
var s = 22;
console.log(pathSum(tree,s));