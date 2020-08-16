from typing import List
# 方法1，二维dp数组
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # base case :
        # dp[0][0] = grid[0][0]
        # dp[0][j] = dp[0][j-1] + grid[0][j]
        # dp[i][0] = dp[i-1][0] + grid[i][0]
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        print(dp)
        return dp[-1][-1]

# 方法二优化，1维度dp数组
class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 空间优化只使用1维数组 ,dp[i-1]代表从左走最小，dp[i]代表从上走最小
        # dp[i] = min(dp[i-1], dp[i])
        # dp[0] = grid[0][0]
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [0] + [float('inf')] * n
        for i in range(m):
            for j in range(n):
                dp[j] = grid[i][j] + min(dp[j - 1], dp[j])
        return dp[-2]