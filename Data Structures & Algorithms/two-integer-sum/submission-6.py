class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        r= len(nums)-1
        curr = 0

        sorted_nums = []

        for i, num in enumerate(nums):
            sorted_nums.append([num,i])

        sorted_nums.sort()

        while l<r:
            curr = sorted_nums[l][0] + sorted_nums[r][0]
            if curr == target:
                return [min(sorted_nums[l][1], sorted_nums[r][1]),
                        max(sorted_nums[l][1], sorted_nums[r][1])]
            elif curr< target:
                l+=1
            else:
                r-=1
