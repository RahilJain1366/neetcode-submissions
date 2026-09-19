class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])

        cache = {0: nums[0], 1 : max(nums[0], nums[1])}

        def backtrack(i):
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] + backtrack(i - 2), backtrack(i - 1))
        
            return cache[i]

        return backtrack(n - 1)