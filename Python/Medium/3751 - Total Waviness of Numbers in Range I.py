# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/description/

class Solution(object):
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness_counter = 0
        for num in map(str, range(num1, num2+1)):
            for i in range(1, len(num)-1):
                if num[i-1] < num[i] > num[i+1]:
                    waviness_counter += 1
                elif num[i-1] > num[i] < num[i+1]:
                    waviness_counter += 1
        return waviness_counter