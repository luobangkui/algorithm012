from typing import List

# 排序 + 扫描， 我写的代码
class Solution:
    def mergeOne(self, res, tp):
        if len(res) == 0:
            res.append(tp)
        elif tp[0] <= res[-1][1] < tp[1] :
            res[-1] = [res[-1][0], tp[1]]
        elif res[-1][1] < tp[1]:
            res.append(tp)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        setinter =list(map(tuple, intervals))
        setinter.sort()
        res = []
        for r in setinter:
            self.mergeOne(res, list(r))
        return res

# 别人的代码
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res