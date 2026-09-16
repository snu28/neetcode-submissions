class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        current_sum = 0
        total_count = 0

        for num in nums:
            current_sum += num
            temp = current_sum - k


            if temp in prefix:
                total_count += prefix[temp]
            
            prefix[current_sum] = prefix.get(current_sum, 0) + 1

        return total_count

        