// There are N children standing in a line. Each child is assigned a rating value.
// You are giving candies to these children subjected to the following requirements:
// • Each child must have at least one candy.
// • Children with a higher rating get more candies than their neighbors.
// What is the minimum candies you must give?
// Example 1:
// Input: [1,0,2]
// Output: 5
// Explanation: You can allocate to the first, second and third child with 2, 1, 2
// candies respectively.
// Example 2:
// Input: [1,2,2]
// Output: 4
// Explanation: You can allocate to the first, second and third child with 1, 2, 1
// candies respectively.
//  The third child gets 1 candy because it satisfies the above two
// conditions.

/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
    var len = ratings.length;
    var right = new Array(len);
    left = new Array(len);

    right[0] = 1;
    left[len-1] = 1;
    for (var i = 1; i < len; i++) {
        if (ratings[i] > ratings[i-1]) right[i] = right[i-1] + 1;
        else right[i] = 1;
    }

    for (var i = len - 2; i >= 0; i--) {
        if (ratings[i] > ratings[i+1]) left[i] = left[i+1] + 1;
        else left[i] = 1;
    }
    var sum = 0;
    for (var i = 0; i < len; i++) {
        sum += Math.max(right[i], left[i]);
    }
    return sum;
    
};
arr = [1,0,2];
console.log(candy(arr));
arr1 = [1,2,2];
console.log(candy(arr1));