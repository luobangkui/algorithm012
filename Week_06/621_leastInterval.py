from typing import List

#真不会做。。。直接抄答案再理解
# 填空的方法
class Solution3:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = 26 * [0]
        for c in tasks:
            m[ord(c)-ord('A')] += 1
        m.sort()
        maxval = m[-1]-1
        idle_slots = maxval * n
        i = 24
        while i >= 0 and m[i] > 0:
            idle_slots -= min(m[i], maxval)
            i -= 1
        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)



#方法一， 排序，每次优先安排次数最多的，n+1为一轮安排任务。然后重复
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = [0] * 26
        for c in tasks:
            m[ord(c)-ord('A')] += 1
        m.sort()
        time = 0
        while m[-1] > 0:
            i = 0
            while i <= n:
                if m[-1] == 0:
                    break
                if i < 26 and m[25-i] > 0:
                    m[25-i] -= 1
                time += 1
                i += 1
            m.sort()
        return time

import heapq
# 方法二优先队列，但是python heapq只能构建小顶堆
class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #优先队列
        m = 26 * [0]
        for c in tasks:
            m[ord(c)-ord('A')] += 1
        heap = []
        for count in m:
            if count > 0:
                heapq.heappush(heap, -count)
        print(heap)
        time = 0
        while heap:
            i = 0
            temp = []
            while i <= n:
                if heap:
                    if -heap[0] > 1:
                        temp.append(-heapq.heappop(heap)-1)
                    else:
                        heapq.heappop(heap)
                time += 1
                if not heap and not temp:
                    break
                i += 1
            for t in temp:
                heapq.heappush(heap, -t)
        return time