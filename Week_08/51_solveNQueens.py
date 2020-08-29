
from typing import List

# 方法一dfs
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(row, cols, xy_diff, xy_sum):
            if row == n:
                queue.append(cols)
                return

            for col in range(n):
                if col not in cols and row + col not in xy_sum and row-col not in xy_diff:
                    dfs(row + 1, cols + [col], xy_diff + [row - col], xy_sum + [row + col])

        queue = []
        dfs(0, [], [], [])
        return [['.'*i + 'Q' + '.' * (n-i-1) for i in cols] for cols in queue]


