# https://leetcode.com/problems/maximum-building-height/description/

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.sort(key=lambda x : x[0])
        current_index, current_height = 1, 0
        max_height = 0

        # if no restrictions
        if not restrictions:
            return n - 1

        # correct from the right if a restriction is unreachable from the previous one
        for i in range(len(restrictions) - 1, 0, -1):
            if restrictions[i - 1][1] > restrictions[i][1] + restrictions[i][0] - restrictions[i - 1][0]:
                restrictions[i - 1][1] = restrictions[i][1] + restrictions[i][0] - restrictions[i - 1][0]

        # add end to restriction when the last restriction isn't the last building, this way the computing goes to the end
        if restrictions[-1][0] < n:
            restrictions.append([n, restrictions[-1][1] + n - restrictions[-1][0]])
        
        # main computing
        for index, height_restriction in restrictions:
            index_diff, height_diff = index - current_index, abs(current_height - height_restriction)
            if index_diff > height_diff:
                max_height = max(max_height, current_height + (height_restriction + index_diff - current_height) // 2)
                current_index, current_height = index, height_restriction
            else:
                current_index = index
                current_height = current_height + index_diff if height_restriction > current_height else current_height - index_diff
                max_height = max(max_height, current_height)
        return max_height