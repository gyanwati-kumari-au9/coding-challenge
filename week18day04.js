// Given an unsorted array of integers nums, return the length of the longest consecutive
// elements sequence.
// Follow up: Could you implement the O(n) solution?
// Example 1:
// Input: nums = [100,4,200,1,3,2]
// Output: 4
// Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore
// its length is 4.
// Example 2:
// Input: nums = [0,3,7,2,5,8,4,6,0,1]
// Output: 9
// Constraints:
// • 0 <= nums.length <= 104
// • -231 <= nums[i] <= 231 - 1

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if(nums.length ==0){
        return 0;
    }
    var count =0,max = 0;
    var arr = nums.slice(0);
    arr.sort((a,b)=>a-b);
    arr.push(Number.NEGATIVE_INFINITY);
    for(var i=1;i<arr.length;i++){
    if(arr[i]==arr[i-1]){
    continue;
    }
    if(arr[i]==arr[i-1]+1){
    count +=1;
    }else{
    max = Math.max(max,count);
    count =0;
    }
    }

    return max+1;
    
};

arr = [100,4,200,1,3,2];
arr1 = [0,3,7,2,5,8,4,6,0,1]
console.log(longestConsecutive(arr));
console.log(longestConsecutive(arr1));