class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        A1 = ((hour + minutes / 60))/ 12 * 360
        A2 = ((minutes / 60) ) * 360
        A1 %= 360
        A2 %= 360        
        return min(abs(A2-A1),360-abs(A2-A1))