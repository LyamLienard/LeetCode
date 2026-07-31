# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/

class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word) < 9: return len(word)
        counts = sorted([word.count(chr(ord("a") + i)) for i in range(26)], reverse=True)
        minimum_key_pushes = 0
        for count_rank, count in enumerate(counts):
            if count:
                minimum_key_pushes += count * (count_rank // 8 + 1)
            else:
                break
        return minimum_key_pushes