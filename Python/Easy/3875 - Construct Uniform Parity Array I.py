# https://leetcode.com/problems/construct-uniform-parity-array-i/description/

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:     
        return True

# Either all numbers are pair, which return True, or there is at least one odd number with which we can make all other number odd, which return True, or all number are odd, which also return True.
# Hence, True is the only possible outcome to this problem since the numbers are distincts.