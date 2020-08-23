from typing import List
# 使用字典树 , 回溯剪枝
class Solution:
    def backtrace(self, i, j, board, root, path, ans):
        node = root
        if '#' in node and node['#'] is True:
            ans.append(path)
            node['#'] = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        # board[i][j] = '@' # return之后就不递归了，影响了board数组
        if tmp not in node:
            return
        # 或者是使用一个visited集合来记录访问过的点
        board[i][j] = '@'
        node = node[tmp]
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            self.backtrace(i+x, j+y, board, node, path+tmp, ans)
        board[i][j] = tmp

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        m, n = len(board), len(board[0])
        for word in words:
            tmp = root
            for w in word:
                tmp = tmp.setdefault(w, {})
            tmp['#'] = True
        ans = []
        for i in range(m):
            for j in range(n):
                self.backtrace(i, j, board, root, '', ans)
        return ans