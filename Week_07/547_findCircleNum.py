from typing import List


# 方法1 dfs
# 时间复杂度，O(N ^ 2)，每个人检查了一次
class Solution1:
    def dfs(self, i, M, visited):
        for j in range(len(M)):
            if j not in visited and M[i][j] == 1:
                visited.add(j)
                self.dfs(j, M, visited)

    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        visited = set()
        count = 0
        m = len(M)
        for i in range(m):
            if i not in visited:
                self.dfs(i, M, visited)
                count += 1
        return count


# 方法二，并查集
# 时间复杂度 ,O(n ^ 3) （ 2重for循环， parent里最坏执行n次）
class Solution2:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        m = len(M)
        p = [i for i in range(m)]
        for i in range(m):
            for j in range(m):
                if M[i][j] == 1:
                    self.union(p, i, j)
        return len(set([self.parent(p,i) for i in range(m)]))

    def union(self,p, i, j):
        # p1 = p[i]
        # p2 = p[j]
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        p[p1] = p2

    def parent(self,p, i):
        # root = p[i]
        root = i
        while root != p[root]:
            root = p[root]
        while i != p[i]:  #压缩
            x = i
            i = p[i]
            p[x] = root
        return root