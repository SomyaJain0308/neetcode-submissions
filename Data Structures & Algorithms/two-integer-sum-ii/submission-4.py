class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 1
        j = len(numbers)
        while True:
            if numbers[0] + numbers[len(numbers) - 1] > target:
                numbers.pop()
                j -= 1
            elif numbers[0] + numbers[len(numbers) - 1] < target:
                numbers.pop(0)
                i += 1
            else:
                return [i, j]