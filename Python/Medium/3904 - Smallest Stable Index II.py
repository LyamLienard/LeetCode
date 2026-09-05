# https://leetcode.com/problems/smallest-stable-index-ii/description/

from itertools import accumulate

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        curr_max = nums[0]
        min_num = list(accumulate(nums[::-1], min))[::-1]
        for i in range(len(nums)):
            curr_max = max(curr_max, nums[i])
            if curr_max - min_num[i] <= k:
                return i
        return -1