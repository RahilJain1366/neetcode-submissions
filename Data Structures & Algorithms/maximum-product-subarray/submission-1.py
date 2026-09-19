class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        maxEnding, minEnding = 1,1

        for num in nums:
            tmp = maxEnding * num
            maxEnding = max(maxEnding * num, minEnding * num, num)
            minEnding = min(tmp, minEnding * num, num)
            res = max(res, maxEnding)

        return res