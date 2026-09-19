class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            
            if token not in ("+", "-", "/", "*"):
                stack.append(int(token))

            if token == "+":
                val = stack.pop()
                stack[-1] += val
            
            elif token == "-":
                val = stack.pop()
                stack[-1] -= val
            
            elif token == "/":
                val = stack.pop()
                stack[-1] = int(stack[-1] / val)
            
            elif token == "*":
                val = stack.pop()
                stack[-1] = stack[-1] * val

        return stack[-1]
