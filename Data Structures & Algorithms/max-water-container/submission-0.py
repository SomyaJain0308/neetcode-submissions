class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        l1 = 0
        l2 = len(height) - 1
        while l2 > l1:
            area = abs(l1 - l2) * min(height[l1], height[l2])    
            max_area = max(max_area, area)
            if height[l1] < height[l2]:
                l1 += 1
            else:
                l2 -= 1
        return max_area