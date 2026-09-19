class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r= len(heights) -1

        res =0

        while l<r:
            temp = (r-l) * min(heights[r],heights[l])
            if temp > res:
                res = temp
            if heights[l] >= heights[r]:
                r-=1
            else:
                l+=1
        
        return res

