# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description/

class Solution:
    def minimumPushes(self, word: str) -> int:
        minimum_key_pushes = 0
        for i in range(len(word)):
            minimum_key_pushes += i // 8 + 1
        return minimum_key_pushes