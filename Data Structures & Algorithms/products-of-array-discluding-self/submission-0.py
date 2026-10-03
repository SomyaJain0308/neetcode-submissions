class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0 for _ in range(len(nums))]
        elif zero_count == 1:
            nums_without_zero = []
            for num in nums:
                if num != 0:
                    nums_without_zero.append(num)
            product_zero = math.prod(nums_without_zero)
        product = math.prod(nums)
        result = []
        for num in nums:
            result.append(product // num) if num != 0 else result.append(product_zero)
        return result