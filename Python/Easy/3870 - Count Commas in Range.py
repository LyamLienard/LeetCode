# https://leetcode.com/problems/count-commas-in-range/

class Solution:
    def countCommas(self, n: int) -> int:
        return n - 999 if n > 999 else 0

# it's a pretty useless problem to solve but it was the daily problem and I solved it, so it gets archived...