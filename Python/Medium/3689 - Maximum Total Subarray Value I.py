# https://leetcode.com/problems/maximum-total-subarray-value-i/description/

class Solution(object):
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums) - min(nums)) * k