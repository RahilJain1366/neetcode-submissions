class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        total = 0
        for token in tokens:

            if token == "+":
                val = stack.pop()
                stack[-1] += val
            elif token == "-":
                val = stack.pop()
                stack[-1] -=val
            elif token == "*":
                val = stack.pop()
                stack[-1] *= val
            elif token == "/":
                val = stack.pop()
                stack[-1] = int(stack[-1] / val)
            else:
                stack.append(int(token))

        return stack[-1]