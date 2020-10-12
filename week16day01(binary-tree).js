// Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to
//     right, level by level).
//     For example:
//     Given binary tree [3,9,20,null,null,15,7],
//     3
//     / \
//     9 20
//     / \
//     15 7
//     return its level order traversal as:
//     [
//     [3],
//     [9,20],
//     [15,7]
//     ]

class Node {
    constructor(val){
        this.val=val;
        this.right=null;
        this.left=null;
    }
}

class BinaryTree{
    constructor(){
        this.root=null;
    }

    insert(val){
        let newNode= new Node (val)
        if (!this.root) this.root=newNode;
        let current =this.root;        
        while (true) {
            if(val === current.val) return undefined;
            if(current.val<val){
                if (current.right===null){
                    current.right=newNode;
                    return this
                }
                    else
                    current=current.right}
            if(current.val>val){
                if (current.left===null){
                    current.left=newNode;
                    return this
                }
                    else
                    current=current.left}
                
        }
    }


}

// class Solution{
//     levelOrder(root){
//         var res = [];
//         if (root == null){
//             return res
//         }
//         var queue = [];
//         queue.push(root);
//         while(queue.length){
//             var level = [];
//             var node = queue.pop(0);
//             level.push(node.x);
//             if (node.left != null){
//                 queue.push(node.left);
//             }
//             if (node.right != null){
//                 queue.push(node.right);
//             }
//             res.push(level);
//         }
//         return res
//     }

//     readTree(arrData){
      
        

//     }
// }

var levelOrder = function(root) {
    const levels = []

    if(!root) {
        return levels
    }

    const queue = [root]
    while (queue.length){
    //    console.log(queue)
       const queueLength = queue.length
       const level = []

       for(let i = 0; i < queueLength; i++){
            
           const node = queue.shift()
        //    console.log(node)
           if(node.left){
               queue.push(node.left)
           }
           if(node.right){
               queue.push(node.right)
           }

           level.push(node.val)
       }
       levels.push(level)
   }
    return levels
}


// s = new Solution();
var inputArr = [3,9,20,null,null,15,7];
// tree=s.readTree(inputArr);

var bt = new BinaryTree();
for (let i=0; i<inputArr.length;i++){
    bt.insert(inputArr[i]);
}
res = levelOrder(bt.root);
console.log(res);