class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        gap = len(nums) // 2
        while gap >= 1:
            for i in range(gap, len(nums)):
                tmp = nums[i]
                j = i - gap
                while j >= 0 and nums[j] > tmp:
                    nums[j + gap] = nums[j]
                    j -= gap
                nums[j + gap] = tmp
            gap //= 2
        return nums
