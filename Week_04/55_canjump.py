from typing import List

# 从后往前贪心
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        endreachable = n-1
        for i in range(n-1,-1,-1):
            if nums[i] + i >= endreachable:
                endreachable = i
        return endreachable == 0