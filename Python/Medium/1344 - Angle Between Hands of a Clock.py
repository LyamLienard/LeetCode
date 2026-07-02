# https://leetcode.com/problems/angle-between-hands-of-a-clock/description/

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        #60 - hour + minutes
        if 0 <= 60 - (hour + minutes / 60) * 5 + minutes < 30:
            return (360 - 360 * (hour % 12 + minutes / 60) / 12 + 360 * minutes / 60) % 360
        #60 - minutes + hour
        elif 0 < 60 - minutes + (hour + minutes / 60) * 5 < 30:
            return 360 - (6 * minutes) + 360 * (hour + minutes / 60) / 12
        #hour - minutes
        elif 60 > 60 - (hour + minutes / 60) * 5 + minutes > 30:
            return 360 * (hour + minutes / 60) / 12 - (360 * minutes / 60)
        #minutes - hour
        elif 60 > 60 - minutes + (hour + minutes / 60) * 5 > 30:
            return 360 * minutes / 60 - 360 * (hour % 12 + minutes / 60) / 12