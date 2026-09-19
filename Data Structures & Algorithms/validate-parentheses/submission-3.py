class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        hashmap = {")":"(", "]":"[","}":"{"}

        for val in s:
            if val in hashmap:
                if stack and hashmap[val] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(val)

        print(stack)
        return len(stack) == 0