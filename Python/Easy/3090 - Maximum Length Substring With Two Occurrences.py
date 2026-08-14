# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left, max_lenght = 0, 1
        counter = [0] * 26
        for i in range(len(s)):
            counter[ord(s[i]) - ord("a")] += 1
            while counter[ord(s[i]) - ord("a")] > 2:
                counter[ord(s[left]) - ord("a")] -= 1
                left += 1
            max_lenght = max(max_lenght, i - left + 1)
        return max_lenght