class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        total = {}
        for num in nums:
            total[num] = total.get(num,0) +1

        heap = []
        for num in total.keys():
            heapq.heappush(heap, (total[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        


        
        
        
        
        