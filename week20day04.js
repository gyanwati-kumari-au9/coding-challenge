// Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of
// the two sorted arrays.
// Follow up: The overall run time complexity should be O(log (m+n)).
// Example 1:
// Input: nums1 = [1,3], nums2 = [2]
// Output: 2.00000
// Explanation: merged array = [1,2,3] and median is 2.
// Example 2:
// Input: nums1 = [1,2], nums2 = [3,4]
// Output: 2.50000
// Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
// Example 3:
// Input: nums1 = [0,0], nums2 = [0,0]
// Output: 0.00000
// Example 4:
// Input: nums1 = [], nums2 = [1]
// Output: 1.00000
// Example 5:
// Input: nums1 = [2], nums2 = []
// Output: 2.00000
// Constraints:
// • nums1.length == m
// • nums2.length == n
// • 0 <= m <= 1000
// • 0 <= n <= 1000
// • 1 <= m + n <= 2000
// • -106 <= nums1[i], nums2[i] <= 106

const findMedianSortedArrays = (nums1,nums2)=> {
    let arr = []
    let totalLength = nums1.length + nums2.length;
    if (totalLength == 1){
        return nums1.length == 1 ? nums1[0] : nums2[0];
    }
    let arrLen = totalLength % 2 == 0 ? (totalLength)/2 + 1 : Math.ceil (totalLength/2);

    let i = 0;
    let j = 0;

    while(arr.length < arrLen){
        if (i < nums1.length && j < nums2.length){
            if(nums1[i] <= nums2[j]){
                arr.push(nums1[i]);
                i++;
            }
            else{
                arr.push(nums2[j]);
                j++;
            }
        }
        else if(i >= nums1.length){
            arr.push(nums2[j]);
            j++;
        }
        else{
            arr.push(nums1[i]);
            i++;
        }
    }
    return totalLength % 2 == 0 ? (arr[arr.length -1] + arr[arr.length - 2])/2 : arr[arr.length -1];
}
n1 = [1,2], n2 = [3,4]
console.log(findMedianSortedArrays(n1,n2));