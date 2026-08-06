# https://leetcode.com/problems/smallest-divisible-digit-product-i/description/

from math import prod

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        return min([i for i in range(n, n + 10) if prod(map(int, str(i) )) % t == 0])