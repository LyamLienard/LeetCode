# https://leetcode.com/problems/count-commas-in-range-ii/

class Solution:
    def countCommas(self, n: int) -> int:
        if len(str(n)) < 4: return 0
        pow_of_thousand = len(str(n)) // 3 + 1 if len(str(n)) % 3 != 0 else len(str(n)) // 3
        comma_count = -1
        for i in range(1, pow_of_thousand + 1):
            if i < pow_of_thousand:
                comma_count += (1000 ** i - 1000 ** (i - 1)) * (i - 1) + 1
            else:
                comma_count += (n - 1000 ** (i - 1)) * (i - 1) + 1
        return comma_count

# I took a different approach to the problem than the submission or editorial answer I've seen and, even tho my answer is visibly worse, still solve it in "0 ms"
# I added the number of comma each power of thousand contributed, while the other counted how many number countributed 1 comma, 2 comma, etc, and added everything
# The official answer is, thanks to its approach, far better :

# class Solution:
#     def countCommas(self, n: int) -> int:
#         p = 1000
#         res = 0
#         while p <= n:
#             res += n - p + 1
#             p *= 1000
#         return res