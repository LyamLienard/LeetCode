# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        char_freq = {"a":0, "b":0, "c":0}
        start = end = counter = 0
        while end < len(s):
            char_freq[s[end]] += 1
            while all(char_freq.values()):
                counter += len(s) - end
                char_freq[s[start]] -= 1
                start += 1
            end += 1
        return counter