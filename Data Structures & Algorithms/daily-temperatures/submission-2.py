class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                stack_temp, stack_id = stack.pop()
                ans[stack_id] = (i - stack_id)

            stack.append((temp, i))

        return ans