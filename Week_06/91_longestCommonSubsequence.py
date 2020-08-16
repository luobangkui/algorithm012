from typing import List


# 方法一，使用两个数组，f1: 表示当前自己作为一个组合， f2: 表示和前一个组合
class Solution1:
    def numDecodings(self, s: str) -> int:
        # f1: 表示当前自己作为一个组合
        # f2: 表示和前一个组合
        if not s or s[0] == '0':
            return 0
        n = len(s)
        f1 = [0] * n
        f2 = [0] * n
        f1[0] = 1
        f2[0] = 0
        for i in range(1, len(s)):
            if s[i] == '0':
                f1[i] = 0
                f2[i] = f1[i-1] if s[i-1] == '1' or s[i-1] == '2' else 0
            else:
                f1[i] = f1[i-1]+f2[i-1]
                f2[i] = f1[i-1] if s[i-1] == '1' or ( s[i-1] == '2' and 0 < int(s[i]) <= 6) else 0
        # print(f1, f2)
        return f1[-1] + f2[-1]


# 方法二，使用一个dp数组
class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] =
        # si ==0 1: 能合起来, 2不能合
        # 此时 1: dp[i] = dp[i-2] 2 dp[i] = 0
        # si != 0  1: 能合， 2不能合
        # 1: dp[i] = dp[i-1]+1 2: dp[i] = dp[i-1]
        if not s or s[0] == '0':
            return 0
        dp = [0] * len(s)
        # 第一个肯定自己编码了
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                # 能合
                if s[i-1] in '12':
                    dp[i] = dp[i-2] if i >= 2 else 1
                else:
                    dp[i] == 0
            else:
                #能合并的话，合并算一种 = dp[i-2]， 单独编码算一种 = dp[i-1] 加起来就是结果
                if s[i-1] == '2' and s[i] in '123456' or (s[i-1] == '1'):
                    dp[i] = dp[i-1] + dp[i-2] if i >= 2 else 2
                else:
                    dp[i] = dp[i-1] if i >= 2 else 1
        return dp[-1]

# 方法3，方法2可以在空间上优化，使用两个变量即可
class Solution3:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        cur, pre = 1, 0
        for i in range(1, len(s)):
            tmp = cur
            if s[i] == '0':
                if s[i-1] in '12':
                    cur = pre if i >= 2 else 1
                else:
                    cur = 0
            else:
                if s[i - 1] == '2' and s[i] in '123456' or (s[i - 1] == '1'):
                    cur = cur + pre if i >= 2 else 2
                else:
                    cur = cur if i >= 2 else 1
            pre = tmp
        return cur
