class Solution:
    def maxArea(self, heights: List[int]) -> int:
    
        left, right = 0, len(heights) - 1
        max_area = float("-inf")
        while left <= right:
            height = min(heights[left], heights[right])
            area = (right - left) * height
            max_area = max(max_area, area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                
        return max_area


