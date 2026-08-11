# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/description/

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0] + 1
        seq_sum, i = nums[0], 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            seq_sum += nums[i]
            i += 1
        nums = set(nums)
        while seq_sum in nums:
            seq_sum += 1
        return seq_sum