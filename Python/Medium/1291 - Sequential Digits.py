# https://leetcode.com/problems/sequential-digits/description/

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_pow10, high_pow10 = len(str(low)) - 1, len(str(high)) - 1
        seq_digits = []
        for current_pow in range(high_pow10 - low_pow10 + 1):
            for seq_digit in range(10 - (low_pow10 + current_pow + 1)):
                temp = "".join([str(seq_digit + 1 + i) for i in range(low_pow10 + current_pow + 1)])
                if low <= int(temp) <= high:
                    seq_digits.append(int(temp))
        return seq_digits