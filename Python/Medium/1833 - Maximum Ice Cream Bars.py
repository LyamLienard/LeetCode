# https://leetcode.com/problems/maximum-ice-cream-bars/description/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i = 0
        while True:
            if i < len(costs) and costs[i] <= coins:
                coins -= costs[i]
                i += 1
            else:
                return i