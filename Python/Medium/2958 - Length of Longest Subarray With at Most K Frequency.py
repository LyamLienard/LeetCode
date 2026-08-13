# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        max_lenght_good_subarray = 1
        left, right, subarray_lenght = 0, 0, 0
        counter = dict()
        while right < len(nums):
            if counter.setdefault(nums[right], 0) == k:
                counter[nums[left]] -= 1
                left += 1
                max_lenght_good_subarray = max(max_lenght_good_subarray, subarray_lenght)
                subarray_lenght -= 1
            else:
                counter[nums[right]] += 1
                right += 1
                subarray_lenght += 1
        max_lenght_good_subarray = max(max_lenght_good_subarray, subarray_lenght)
        return max_lenght_good_subarray