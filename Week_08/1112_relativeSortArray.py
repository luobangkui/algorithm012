from collections import Counter
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counters = Counter(arr1)
        tmp = []
        for a in arr2:
            tmp.extend([a] * counters[a])
            counters.pop(a)
        for k in sorted(counters.keys()):
            tmp.extend([k] * counters[k])
        return tmp