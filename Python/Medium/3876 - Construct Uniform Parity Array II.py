# https://leetcode.com/problems/construct-uniform-parity-array-ii/

class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        return bool(min(nums) & 1) or not(any(num & 1 for num in nums))