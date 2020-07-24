from typing import List


# 又是一脸懵逼的回溯题，它这个去重的方式还得多做几遍好好理解一下
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = []
        def dfs(level,length,cur, seen,nums):
            if level == length:
                res.append(cur[:])
                return
            for i in range(length):
                if not i in seen:
                    if i > 0 and nums[i-1] == nums[i] and i-1 not in seen:
                        continue
                    seen.add(i)
                    cur.append(nums[i])
                    dfs(level+1,length,cur,seen,nums)
                    seen.remove(i)
                    cur.pop()
        nums.sort()
        dfs(0,len(nums),[],set(),nums)
        return res