# https://leetcode.com/problems/path-existence-queries-in-a-graph-i/description/

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        memory = [None] * n
        answer = [True] * len(queries)
        if n > 1:
            for i in range(n - 1):
                memory[i] = nums[i + 1] <= nums[i] + maxDiff
        for i in range(len(queries)):
            if queries[i][0] == queries[i][1]:
                continue
            elif not all(memory[min(queries[i][0], queries[i][1]):max(queries[i][0], queries[i][1])]):
                answer[i] = not(answer[i])
        return answer