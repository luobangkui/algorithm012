
class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] 表示第i个字符能够解码的最大总数
        # dp[i] 跟i和i-1的字符有关，如果i和i-1可以合并，那就是合并+单独处理的个数，dp[i] = dp[i-2](合并) + dp[i-1](不合并个数)
        # 如果不能合并 dp[i] = dp[i-1]
        if not s:
            return 0

        n = len(s)
        dp = [0] * n + [1]
        dp[0] = 0 if s[0] == '0' else 1
        for i in range(1, n):
            # 如果不能合并，表示最后一个字符要单独成为一个编码
            if not 1 <= int(s[i-1:i+1]) <= 26 or s[i-1] == '0':
                if s[i] == '0': #最后一个字符0无法单独编码
                    dp[i] = 0
                else:
                    dp[i] = dp[i-1]
            else:#如果能合并，那就是合并前dp[i-2] + 不合并dp[i-1]
                if s[i] == '0': #为0，无法单独编码
                    dp[i] = dp[i-2]
                else:
                    dp[i] = dp[i-2] + dp[i-1]
        return dp[-2]