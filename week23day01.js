// Given an unsorted integer array nums, find the smallest missing positive integer.
// Follow up: Could you implement an algorithm that runs in O(n) time and uses constant
// extra space.?
// Example 1:
// Input: nums = [1,2,0]
// Output: 3
// Example 2:
// Input: nums = [3,4,-1,1]
// Output: 2
// Example 3:
// Input: nums = [7,8,9,11,12]
// Output: 1
// Constraints:
// • 0 <= nums.length <= 300
// • -231 <= nums[i] <= 231 - 1

var firstMissingPositive = function(nums) {
    let map = {}
    let max = 0
    nums.map((res) => {
        map[res] ? map[res]++ : map[res] = 1
        max = Math.max(max, res)
    })
    
    if (max <= 0) {
        return 1
    }
    
    for (let i = 1; i <= max + 1; i++) {
        if (!map[i]) return i 
    }
};

nums = [1,2,0];
// nums = [3,4,-1,1];
console.log(firstMissingPositive(nums));