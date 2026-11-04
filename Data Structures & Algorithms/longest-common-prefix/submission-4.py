class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for s in strs[1:]:
            for i in range(len(res)):
                if i < len(s):
                    if res[i] != s[i]:
                        res = res[:i]
                        break
                else:
                    res = s
                    break
        return res