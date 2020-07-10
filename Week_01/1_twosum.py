from typing import  List

# 方法一，二重循环暴力查找
# 时间复杂度 O(n^2)
# 空间复杂度 O(1)
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ln = len(nums)
        for i in range(ln):
            for j in range(ln):
                if j != i and nums[i] + nums[j] == target:
                    return [i,j]
        return []

#方法2，用哈希表，先遍历一遍nums，target-v做key，数组下标作为value
# 第二遍遍历，满足 v in hash[v] and hash[v] != i，返回hash[v]和i
# 时间复杂度O(n)，因为只需要遍历两次数组
# 空间复杂度O(n)，使用hash表存数组信息
# 看了高赞的答案，其实代码可以写到一个循环里面去

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i,v in enumerate(nums):
            hash[v] = i
        for i,v in enumerate(nums):
            if (target-v) in hash and hash[target-v] != i:
                return [i,hash[target-v]]


class Solution2Opt:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i,v in enumerate(nums):
            if (target-v) in hash and hash[target-v] != i:
                return hash[target-v],i
            hash[v] = i