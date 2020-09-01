
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # (())
        # dp[i] 表示以i结尾，的最长有效括号长度
        # dp[i]  i,i-1 = ()       dp[i] = dp[i-2] + 2
        # dp[i]  i, i-1 = ))      dp[i] = dp[i-1] + 2    if s[i-dp[i-1]-1] = '('
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        maxval = 0
        for i in range(1, n):
            if s[i-1:i+1] == '()':
                dp[i] = dp[i-2] + 2
            elif s[i-1:i+1] == '))' and i-dp[i-1] - 1 >= 0 and s[i-dp[i-1] - 1] == '(':
                dp[i] = dp[i-1] + 2 if i-dp[i-1] - 1 == 0 else dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
            maxval = max(dp[i], maxval)
        return maxval

# 贪心法，左右括号计数
class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        #贪心法
        if not s:
            return 0
        n = len(s)
        left, right = 0, 0
        maxval = 0
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxval = max(maxval, left * 2)
            elif right > left:
                left, right = 0, 0
        left, right = 0, 0
        for i in range(n-1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
            if right == left:
                maxval = max(maxval, right * 2)
            elif left > right:
                left, right = 0, 0
        return maxval