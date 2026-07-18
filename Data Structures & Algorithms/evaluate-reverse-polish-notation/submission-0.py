class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            try:
                num = int(token)
                stack.append(num)
            except ValueError:
                right = stack.pop()
                left = stack.pop()

                if token == '+':
                    res = left + right
                elif token == '-':
                    res = left - right
                elif token == '*':
                    res = left * right
                elif token == '/':
                    res = int(left / right)
                stack.append(res)

        return stack[-1]

