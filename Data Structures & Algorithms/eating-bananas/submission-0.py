class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_element = max(piles)
        min_k = float('inf')
        l, r = 1, max_element
        while l <= r:
            isHoursExceeded = False
            k = (r + l) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
                if hours > h:
                    isHoursExceeded = True
                    break
            if not isHoursExceeded:
                min_k = k
                r = k - 1
            if isHoursExceeded:
                l = k + 1
        return min_k