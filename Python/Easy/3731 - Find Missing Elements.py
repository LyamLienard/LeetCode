# https://leetcode.com/problems/find-missing-elements/description/

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        return sorted(list(set(range(min(nums), max(nums) + 1)).difference(set(nums))))