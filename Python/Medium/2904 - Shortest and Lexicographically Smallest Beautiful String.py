# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/description/

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k: return ""
        memory = s
        for i in range(len(s)):
            if s[i] == "1":
                counter, j = 1, 1
                while counter < k and i + j != len(s):
                    if s[i + j] == "1":
                        counter += 1
                    j += 1
                if counter == k and (j < len(memory) or j == len(memory) and s[i:i + j] < memory):
                    memory = s[i:i + j]
        return memory