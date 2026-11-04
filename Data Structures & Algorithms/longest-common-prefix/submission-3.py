class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0] or ""
        for s in strs:
            for i in range(len(res)):
                if i < len(s):
                    if res[i] != s[i]:
                        res = res[:i]
                        if res == "":
                            return ""
                        break
                else:
                    res = s
                    break
        return res