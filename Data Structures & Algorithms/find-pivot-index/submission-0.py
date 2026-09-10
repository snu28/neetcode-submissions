class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            curr = i
            left=0
            right=0

            if curr!=0:
                for j in range(curr-1,-1, -1):
                    left+=nums[j]

            if curr!=len(nums)-1:
                for k in range(curr+1,len(nums)):
                    right+=nums[k]
            
        
            if left == right:
                return i
        
        return -1