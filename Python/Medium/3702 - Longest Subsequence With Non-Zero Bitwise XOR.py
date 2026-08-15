# https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/description/

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        return len(nums) if ([acc := 0] + [acc := acc ^ num for num in nums])[-1] else (len(nums) - 1) * any(nums)

# First medium solve with oneliner ! It's not that optimised but not too bad either