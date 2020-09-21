#Q.https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        top_k = nums[0:k]
        top_k.sort(reverse = True)

        for i in nums[k:]:
            if i > top_k[-1]:
                top_k.pop() 
                top_k.append(i) 
                top_k.sort(reverse = True) 

        return top_k[-1]
   