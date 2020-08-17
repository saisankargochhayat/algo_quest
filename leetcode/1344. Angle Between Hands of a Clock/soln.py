class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hdeg = ((hour*30) + (minutes*0.5))%360
        mdeg = (minutes * 6)
        angle = abs(hdeg-mdeg)
        return min(angle, 360-angle)
