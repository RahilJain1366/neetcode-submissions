class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        freq = Counter(nums)

        bucket = [[] for _ in range(n + 1)]

        for num, count in freq.items():
            bucket[count].append(num)

        res = []

        for count in range(n, 0, -1):
            for num in bucket[count]:
                res.append(num)

            if len(res) == k:
                return res


