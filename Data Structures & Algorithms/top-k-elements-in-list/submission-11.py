class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = collections.Counter(nums)
        res = []
        heap = []

        for num, count in counter.items():
            heapq.heappush(heap, (-count, num))

        
        while k > 0:
            
            res.append(heapq.heappop(heap)[1])
            k -= 1

        return res
