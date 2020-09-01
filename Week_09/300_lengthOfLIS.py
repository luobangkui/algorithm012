from typing import List

# 动态规划n^2时间复杂度
class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# 贪心 +  二分法 nlogn时间复杂度
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                # 贪心 + 二分，
                # d 的i位置保持，当前长度的，递增序列的最小的符合值
                # 是一个关于下标i的单调增函数
                l, r = 0, len(d) - 1
                loc = r #最后n落到的位置
                while l <= r:
                    mid = (l + r) >> 1
                    if n <= d[mid]:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)