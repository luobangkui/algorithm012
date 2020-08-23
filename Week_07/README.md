## 学习笔记

### 作业

[括号生成](https://github.com/luobangkui/algorithm012/blob/master/Week_07/22_generateParenthesis.py)

[单词接龙](https://github.com/luobangkui/algorithm012/blob/master/Week_07/127_ladderLength.py)

[实现前缀树](https://github.com/luobangkui/algorithm012/blob/master/Week_07/208_Trie.py)

[单词搜索II](https://github.com/luobangkui/algorithm012/blob/master/Week_07/212_findWords.py)

[最小基因变化](https://github.com/luobangkui/algorithm012/blob/master/Week_07/433_minMutation.py)

[朋友圈](https://github.com/luobangkui/algorithm012/blob/master/Week_07/547_findCircleNum.py)

[岛屿数量](https://github.com/luobangkui/algorithm012/blob/master/Week_07/200_numIslands.py)

[有效的数独](https://github.com/luobangkui/algorithm012/blob/master/Week_07/36_isValidSudoku.py)

[N皇后](https://github.com/luobangkui/algorithm012/blob/master/Week_07/51_solveNQueens.py)

[解数独](https://github.com/luobangkui/algorithm012/blob/master/Week_07/37_solveSudoku.py)



<br><br><br>

这一期的题目大部分是之前dfs和bfs里面做过的题目，但是这次做还是会卡住。

主要是边界值条件，和细节的方面容易挖坑。导致半天想不出来是哪里的问题，可能代码基本写完了，但是差在某处细节导致结果不过。比如单词搜索这里，
标记访问过的board[i][j]，自己提前改变board[i][j]值然后导致结果错误
```
        tmp = board[i][j]
        # board[i][j] = '@' # return之后就不递归了，影响了board数组
        if tmp not in node:
            return
        board[i][j] = '@'
```

还有一种情况是完全思路不对，比如被围绕的区域这道题目。这种只能参考题解了

题目还是多做几遍，而且在细节的地方还多需要加强。 同时要学会课上之前说的自顶向下的编程方式





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