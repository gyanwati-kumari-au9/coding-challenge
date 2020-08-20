#Q.https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums,0,len(nums)-1,k)
    
    def quickSelect(self,nums,start,n,k):
        pos = self.kthElement(nums,start,n)
        if pos == k-1:
            return nums[pos]
        elif pos >= k:
            return self.quickSelect(nums,start,pos-1,k)
        return self.quickSelect(nums,start,pos+1,k)
    
    def kthElement(self,nums,left,right):
        x = nums[right]
        i = left
        for j in range (left,right):
            if nums[j]>x:
                nums[j],nums[i]=nums[i],nums[j]
                i += 1
            nums[right],nums[i]=nums[i],nums[right]
        return i