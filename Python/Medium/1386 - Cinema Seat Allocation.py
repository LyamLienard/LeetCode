# https://leetcode.com/problems/cinema-seat-allocation/description/

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        group_counter = 2 * n
        reserved_seats = dict()
        for row, seat in reservedSeats:
            if seat not in (1, 10):
                if reserved_seats.get(row, False):
                    reserved_seats[row].add(seat)
                else:
                    reserved_seats[row] = {seat}

        for row in reserved_seats.keys():
            group_counter -= 1
            if not {2, 3, 4, 5}.isdisjoint(reserved_seats[row]) and not {6, 7, 8, 9}.isdisjoint(reserved_seats[row]) and not {4, 5, 6, 7}.isdisjoint(reserved_seats[row]):
                group_counter -= 1
        return group_counter