# https://leetcode.com/problems/left-and-right-sum-differences/description/

class Solution(object):
    def leftRightDifference(self, nums):
        nums_lenght = len(nums)
        leftSum = [sum(nums[:i]) for i in range(nums_lenght)]
        rightSum = [sum(nums[:i:-1]) for i in range(nums_lenght)]
        return [abs(leftSum[i] - rightSum[i]) for i in range(nums_lenght)]
    
# Compact alternative, for fun :
# class Solution(object):
#     def leftRightDifference(self, nums):
#         nums_lenght = len(nums)
#         return [abs(left - right) for left, right in zip([sum(nums[:i]) for i in range(nums_lenght)], [sum(nums[:i:-1]) for i in range(nums_lenght)])]