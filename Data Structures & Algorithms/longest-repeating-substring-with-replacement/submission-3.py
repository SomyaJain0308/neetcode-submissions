class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0
        freq = {}
        l, r = 0, 0
        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            count = r - l + 1
            max_freq = max(freq.values()) if freq.values() else 0 # Max O(26n)
            if count - max_freq > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            r += 1
            if max_count < count and count <= k + max_freq:
                max_count = count
        return max_count
