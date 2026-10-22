class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l, r = 0, len(s1) - 1
        freq1 = [0] * 26
        for char in s1:
            freq1[ord(char) - ord("a")] += 1

        for i in range(len(s2)):
            freq2 = [0] * 26
            for j in range(l, r + 1):
                freq2[ord(s2[j]) - ord("a")] += 1
            if freq1 == freq2:
                return True 
            l += 1
            r += 1 
            if not r < len(s2): 
                return False