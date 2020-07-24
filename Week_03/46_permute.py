from  typing import List

# 回溯算法，实在是看不懂，多写几遍吧...

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(first):
            if first == n-1:
                res.append(nums[:])
                return
            for i in range(first,n):
                nums[i],nums[first] = nums[first],nums[i]
                backtrack(first + 1)
                # backtrack
                nums[i], nums[first] = nums[first], nums[i]
        backtrack(0)
        return res