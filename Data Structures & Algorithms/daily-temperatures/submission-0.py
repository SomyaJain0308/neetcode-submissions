class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        def check(j: int, result: list[int]) -> int:
            if result[i - j] != 0:
                j += 1
                return check(j, result)
            else:
                return j
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            j = 0
            while stack and temp > stack[-1]:        
                j += 1 
                j = check(j, result)
                result[i - j] = j
                stack.pop()
            stack.append(temp)
        return result