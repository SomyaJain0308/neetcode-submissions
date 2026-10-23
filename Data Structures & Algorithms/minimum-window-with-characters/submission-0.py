class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_str = ""
        if len(t) > len(s):
            return min_str
        freq = {}
        for i, char in enumerate(t):
            freq[char] = freq.get(char, 0) + 1
        count = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] in freq:
                if freq[s[r]] > 0:
                    count += 1
                freq[s[r]] -= 1
            while count == len(t):
                if min_str == "":
                    min_str = s[l:r + 1]
                current_str = s[l:r + 1]
                if len(min_str) > len(current_str):
                    min_str = current_str
                if s[l] in freq:
                    freq[s[l]] += 1
                    if freq[s[l]] > 0:
                        count -= 1
                l += 1
            r += 1
        return min_str