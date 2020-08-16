
# 动态规划
#
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = []
        lens = len(s)
        if lens == 0:return 0
        for i in range(lens):
            dp.append(0)
        for i in range(1,lens):
            if s[i-1:i+1] == "()":
                if i == 1:
                    dp[i] = 2
                else:
                    dp[i] = dp[i-2] + 2
            if s[i-1:i+1] == "))":
                if i - dp[i-1] - 2 >=0:
                    if s[i - dp[i-1] - 1] == "(":
                        dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]
                        continue
                if i - dp[i-1] - 1 == 0 and s[i - dp[i-1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2
        return max(dp)
# 代码优化减少行数
class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        maxdp = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = (dp[i - 1] + dp[i - dp[i - 1] - 2] + 2) if i - dp[i - 1] - 2 >= 0 else dp[i - 1] + 2
                maxdp = max(maxdp, dp[i])
        return maxdp