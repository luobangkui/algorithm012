
# 二分法
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:return 0
        if x == 1:return 1

        l, r, y= 0, x, 0
        while l <= r:
            y = (l+r)//2
            if y*y == x or (y*y < x and (y+1)**2 > x):
                return y
            if y*y < x:
                l = y + 1
            else:
                r = y - 1
        return