class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        result = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                scores.append(scores[-2] + scores[-1])
            elif operations[i] == "D":
                scores.append(2 * scores[-1])
            elif operations[i] == "C":
                scores.pop()
            else:
                scores.append(int(operations[i]))
        for num in scores:
            result += int(num)
        return result