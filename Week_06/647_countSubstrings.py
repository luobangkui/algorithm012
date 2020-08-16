
class Solution:
    def countSubstrings(self, s: str) -> int:
        # 动态规划方法
        # dp[i][j] = dp[i-1][j-1] and s[i-1] == s[j-1]
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        count = n
        for i in range(n-1, -1, -1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    #
                    if j-i == 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                count += 1 if dp[i][j] else 0
        return count



# 方法1，暴力法，n^2 时间复杂度
class Solution(object):
    def countSubstrings(self, S):
        N = len(S)
        ans = 0
        for center in range(2 * N - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

#manager算法
class Solution2(object):
    def countSubstrings(self, S):
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            center = right = 0
            for i in range(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z
        return sum((v+1)//2 for v in manachers(S))