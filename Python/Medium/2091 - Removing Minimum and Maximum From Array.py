# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        if min_index == max_index: return min_index + 1 # this line is only useful if there's a non-negligable number of single number list passed in, which seems to be the case in LeetCode's test cases here
        return min(
            max(max_index, min_index) + 1, 
            len(nums) - min(min_index, max_index), 
            min(min_index, max_index) + 1 + len(nums) - max(max_index, min_index)
            )
# One observation worth noting here is that using list.index(x) and min/max(list) twice each is actually faster than going through nums once to find everything.
# I though otherwise at first and went with a loop over indexes of nums with 2 variable to keep track of min and max indexes but couldn't obtain reasonnable times compared to everyone else
# Whether this is due to under-the-hood python optimization or LeetCode's test cases is not entirely clear but I would bet on the former