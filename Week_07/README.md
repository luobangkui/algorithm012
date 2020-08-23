学习笔记



### 字典树模板 + 单词搜索
```
from  typing import List
class Trie:

    def __init__(self):
        self.root = {}
        self.end_word = "#"

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.end_word] = self.end_word

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.end_word in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, '', ans)
        return ans

    def dfs(self, board, node, i, j, path, ans):
        if '#' in node and node['#'] == '#':
            ans.append(path)
            node['#'] = '@'
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        if tmp not in node:
            return
        node = node[tmp]
        board[i][j] = '@'
        self.dfs(board, node, i + 1, j, path + tmp, ans)
        self.dfs(board, node, i - 1, j, path + tmp, ans)
        self.dfs(board, node, i, j - 1, path + tmp, ans)
        self.dfs(board, node, i, j + 1, path + tmp, ans)
        board[i][j] = tmp
```

##### 时间复杂度分析
1. 建立字典树，需要遍历整个words，t1 = N =  sum(len(words))

2. dfs 搜索，每一层dfs调用执行的时间可以看做是O(1)，因为字典树查找O(1)，下一层的dfs是4次，递归一个单词，相当于是 4 ^ k

3. 节点遍历是O(m * n)

所以时间复杂度是T = O(m * n * 4^k)