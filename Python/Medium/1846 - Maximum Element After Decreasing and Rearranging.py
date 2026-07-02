# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/description/

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                continue
            else:
                arr[i] = arr[i-1] + 1
        return max(arr)