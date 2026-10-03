class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        nums_set = set(nums)
        for num in nums:
            if num - 1 not in nums_set:
                seq = 1
                while num + 1 in nums_set:
                    seq += 1
                    num += 1
                if seq > longest_seq:
                    longest_seq = seq
        return longest_seq