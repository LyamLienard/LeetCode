# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_dist = None
        first_crit_point, prev_crit_point, latest_crit_point = None, None, None
        prev, curr, foll = head, head.next, head.next.next
        i = 2
        while foll is not None:
            if prev.val > curr.val < foll.val or prev.val < curr.val > foll.val: # is faster than (curr.val - prev.val) * (curr.val - foll.val) > 0
                if first_crit_point is None:
                    first_crit_point, prev_crit_point = i, i
                else:
                    if latest_crit_point is not None:
                        prev_crit_point = latest_crit_point
                    latest_crit_point = i
                    min_dist = min(min_dist, latest_crit_point - prev_crit_point) if min_dist is not None else latest_crit_point - prev_crit_point
            i += 1
            prev, curr, foll = curr, foll, foll.next
        if latest_crit_point is None:
            return [-1, -1]
        else:
            return min_dist, latest_crit_point - first_crit_point