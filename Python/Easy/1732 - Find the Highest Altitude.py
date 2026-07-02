# https://leetcode.com/problems/find-the-highest-altitude/description/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        counter = 1
        gain = [0] + gain
        while counter < len(gain):
            gain[counter] = gain[counter - 1] + gain[counter]
            counter += 1
        return max(gain)