
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #   s[:i]有多少种得到t[:j]的方案         (s[i]算到子序列里)  s[i]不算到子序列里
        # dp[i][j] = dp[i-1][j-1]   + dp[i-1][j] if s[i] == t[j]           s[i] == t[j]
        # dp[i][j] = dp[i-1][j]                       else
        # t\s
        # base case  j == 0  dp[i][0] = 1
        #            i == 0  dp[0][1...n] = 0
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]