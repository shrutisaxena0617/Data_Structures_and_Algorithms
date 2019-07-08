class Solution:
  def angleClock(self, h, m):
    if h and m:
      if h<0 or m<0 or h>12 or m>60:
        return -1
      else:
        if h==12:
            h=0
        if m==60:
            m=0
        hour_angle = (60*h+m)*0.5
        minute_angle = 6*m
        res = abs(hour_angle - minute_angle)
        return min(res, 360-res)

sol = Solution()
res = sol.angleClock(12,30)
print(res)


9425651102


#!s**ib**e
#opt mcowens , iglobal, photo, scans, i-983 fill for elena, appointment with robert
# 
