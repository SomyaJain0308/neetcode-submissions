class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set("+-*/")
        stack = []
        result = int(tokens[0])
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:                        
                second = stack.pop()
                first = stack.pop()
                if token == "+": 
                    result = first + second
                elif token == "-":
                    result = first - second
                elif token == "*":
                    result = first * second
                else:
                    result = int(first / second)
                stack.append(result)
        return result