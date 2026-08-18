# https://leetcode.com/problems/find-the-largest-almost-missing-integer/description/

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        elif k == 1:
            counter = [0] * (max(nums) + 1)
            for i in nums:
                counter[i] += 1
            one_counts = [i for i in range(len(counter)) if counter[i] == 1]
            return max(one_counts) if one_counts else -1
        else:
            return max(nums[0] if nums[0] not in nums[1:] else -1, nums[-1] if nums[-1] not in nums[:-1] else -1)