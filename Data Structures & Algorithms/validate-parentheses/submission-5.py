class Solution:
    def isValid(self, s: str) -> bool:
        opening_parentheses = set("({[")
        closing_parentheses = set(")}]")
        stack = []
        for char in s:
            if not stack and char in closing_parentheses:
                return False
            if char in opening_parentheses:
                stack.append(char)
            elif char in closing_parentheses:
                if stack[-1] == "[" and char != "]":
                    return False
                elif stack[-1] == "{" and char != "}":
                    return False
                elif stack[-1] == "(" and char != ")":
                    return False
                stack.pop()
        if not stack:
            return True
        return False