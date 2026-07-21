# https://leetcode.com/problems/maximize-active-section-with-trade-i/description/

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        if len(s) < 3: return sum([1 if char == "1" else 0 for char in s])
        simplified_s = []
        s = "1" + s + "1"

        prev_char = True
        counter = 0
        for i, char in enumerate(s):
            if (char == "1" and prev_char) or (char == "0" and not prev_char):
                counter += 1
            elif (char == "1" and not prev_char) or (char == "0" and prev_char):
                simplified_s.append(counter)
                counter = 1
                prev_char = not prev_char
            if i == len(s) - 1:
                simplified_s.append(counter)

        if len(simplified_s) < 5:
            return sum([1 if char == "1" else 0 for char in s]) - 2

        simplified_s[0] -= 1
        if len(simplified_s) % 2 == 1: simplified_s[-1] -= 1
        max_n_of_zeros = 2
        for i in range(0, len(simplified_s) - 4, 2):
                max_n_of_zeros = max(simplified_s[i + 1] + simplified_s[i + 3], max_n_of_zeros)
        return sum(simplified_s[::2]) + max_n_of_zeros
