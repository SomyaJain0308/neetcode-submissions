class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < len(nums):
            if nums[i] == val:
                nums[i] = nums[n - 1]
                nums.pop()
                i -= 1
                n -= 1
            i += 1
        return len(nums)