from  typing import List


# 这道题可以想成扫雷游戏那种，思想就是把连着的1(炸弹)，全部点爆。

class Solution:
    def dfs(self, grid, i, j, n, m):
        if i < 0 or j < 0 or i >= n or j >= m:
            return
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i - 1, j, n, m)
        self.dfs(grid, i + 1, j, n, m)
        self.dfs(grid, i, j - 1, n, m)
        self.dfs(grid, i, j + 1, n, m)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    # 全都置成0
                    self.dfs(grid, i, j, n, m)
        return count