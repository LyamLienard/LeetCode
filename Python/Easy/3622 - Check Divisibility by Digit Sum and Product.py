# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/description/

from math import prod

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        return True if not n % (sum(map(int, str(n))) + prod(map(int, str(n)))) else False