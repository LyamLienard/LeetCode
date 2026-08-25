# https://leetcode.com/problems/smallest-missing-multiple-of-k/description/

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        return (lambda s: next(i * k for i in range(1, 102) if i * k not in s))(set(nums))

# same as return next(i * k for i in range(1, 102) if i * k not in set(nums)) but the set isn't recreated each time, that is the sole point of the lambda function trick
# (otherwise using the list would actually be faster as creating the set is O(n) and accessing it is O(1) whereas searching in an existing list is O(i) i being the target, with the worst case being O(n))
