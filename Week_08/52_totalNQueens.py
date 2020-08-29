# 位运算方法
class Solution:
    def dfs(self, n, row,  cols, hd, dd):
        if row >= n:
            self.count += 1
            return

        bits = (~ (cols | hd | dd)) & ((1<<n) - 1)

        while bits:
            p = bits & -bits # 取最低位1
            bits = bits & (bits - 1) # 标识p位置放上皇后
            self.dfs(n, row + 1, cols | p, (hd |p) << 1, (dd | p) >> 1)


    def totalNQueens(self, n: int) -> int:
        self.count = 0
        self.dfs(n, 0, 0, 0, 0)
        return self.count


from typing import List

# 方法二dfs
class Solution2:
    def totalNQueens(self, n: int) -> int:
        def dfs(row, cols, xy_diff, xy_sum):
            if row == n:
                self.count += 1
                return

            for col in range(n):
                if col not in cols and row + col not in xy_sum and row-col not in xy_diff:
                    dfs(row + 1, cols + [col], xy_diff + [row - col], xy_sum + [row + col])
        self.count = 0
        dfs(0, [], [], [])
        return self.count