# 使用hash表，执行时间2n，时间复杂度O(n)，进行了2次遍历
# 空间复杂度O(n)

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return 0
        hash = {}
        for i,v in enumerate(nums):
            hash[v] = i
        for i,v in enumerate(nums):
            if target - v  in hash and hash[target-v] != i:
                return [hash[target-v],i]
        return []