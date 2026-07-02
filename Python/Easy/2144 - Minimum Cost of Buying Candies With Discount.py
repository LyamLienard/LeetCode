# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/

class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse = True)
        total_cost = 0
        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                total_cost += cost[i]
        return total_cost