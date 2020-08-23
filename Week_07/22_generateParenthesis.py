from typing import List


# dfs剪枝
class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        ans = []

        def dfs(l, r, path, ans):
            if l == n and r == n:
                ans.append(path)
            if l < n:
                # 加左括号
                dfs(l+1, r, path + '(', ans)
            if l <= n and r < l:
                # 加右括号
                dfs(l, r+1, path + ')', ans)
        dfs(0, 0, '', ans)
        return ans

# 动态规划
class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        total_1 = []
        total_1.append([None]) # 0组括号记录none
        total_1.append(['()']) # 1组()
        for i in range(2, n+2):
            l = []
            for j in range(i):
                now_list1 = total_1[j] # p = j 时的括号组合情况
                now_list2 = total_1[i-1-j] # q = (i-1) - j 时的括号组合情况
                for k1 in now_list1:
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ''
                        if k2 == None:
                            k2 = ''
                        el = '(' + k1 + ')' + k2
                        l.append(el)
            total_1.append(l)
        return total_1[n]