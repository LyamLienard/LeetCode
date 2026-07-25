# https://leetcode.com/problems/maximum-product-of-two-digits/description/

class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        while n != 0:
            right_most_digits = n % 10
            digits.append(right_most_digits)
            n //= 10
        digits.sort(reverse=True)
        return digits[0] * digits[1]