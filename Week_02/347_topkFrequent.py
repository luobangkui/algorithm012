
# 转化成计数，然后问题变成最大的k个数
# 最大k个数，维护长度是k的小顶堆，最小k个数，维护长度k的大顶堆
# 时间复杂度O(n) = nlogk
# 空间复杂度O(k)

from typing import List
from collections import Counter
import heapq
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap,res = [],[]
        print(counter)
        for key in counter.keys():
            if len(heap) == k:
                if counter[key] > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(counter[key],key))
            else:
                heapq.heappush(heap, (counter[key], key))
        return [ c[1] for c in heap]