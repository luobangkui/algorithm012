from collections import defaultdict, deque
from typing import List
import string

# 精简版双向bfs， 直接学习这个代码，拿来记住了
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        bq, eq, length = {beginWord}, {endWord}, len(beginWord)
        wordList = set(wordList)
        dis = 1
        while bq and eq:
            nq = set()
            dis += 1
            for word in bq:
                for i in range(length):
                    for c in string.ascii_lowercase:
                        if c != word[i]:
                            x = word[:i] + c + word[i+1:]
                            if x in eq:
                                return dis
                            if x in wordList:
                                nq.add(x)
                                wordList.remove(x)
            bq = nq
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return 0


# 方法一，官方版双向dfs，代码略冗长
class Solution1:
    def __init__(self):
        self.all_combo = defaultdict(set)
        self.length = 0

    def travel(self, q, visited, other_visited):
        beginword, time = q.popleft()
        for i in range(self.length):
            curword = beginword[:i] + '_' + beginword[i+1:]
            for s in self.all_combo[curword]:
                if s not in visited:
                    if s in other_visited:
                        return time + other_visited[s]
                    else:
                        visited[s] = time + 1
                        q.append((s, time + 1))
        return None

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        self.length = len(beginWord)
        # all_combo 添加所有组合情况
        for word in wordList:
            for i in range(self.length):
                self.all_combo[word[:i] + '_' + word[i+1:]].add(word)

        bq, eq = deque(),deque()
        bq.append((beginWord,1))
        eq.append((endWord,1))
        bvisited, evisited = {beginWord: 1}, {endWord: 1}
        ans = None
        while bq and eq:
            # 双向广度优先
            ans = self.travel(bq, bvisited, evisited)
            if ans:
                return ans
            ans = self.travel(eq, evisited, bvisited)
            if ans:
                return ans
        return 0

# 方法二，双向bfs，使用两个bq和eq， 然后每次交换
class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList:
            return 0
        all_combo, length = defaultdict(set), len(beginWord)
        for word in wordList:
            for i in range(length):
                all_combo[word[:i] + '_' + word[i+1:]].add(word)
        bq, eq, nq = {beginWord: 1}, {endWord: 1}, {}
        bqseen, eqseen, rev = set(), set(), False
        while bq:
            for w in bq:
                for i in range(length):
                    nk = w[:i] + '_' + w[i+1:]
                    if nk in all_combo:
                        for s in all_combo[nk]:
                            if s in bqseen:
                                continue
                            if s in eq:
                                return eq[s] + bq[w]
                            else:
                                bqseen.add(s)
                                nq[s] = bq[w] + 1
            bq, nq = nq, {}
            if len(bq) > len(eq):
                bq, eq, bqseen, eqseen = eq, bq, eqseen, bqseen
        return 0


# 方法3 单向bfs，对比双向执行时间略长，但是代码简略
class Solution3:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or not endWord in wordList:return 0
        q, seen, length, words = {beginWord}, set(), len(beginWord),  set(wordList)
        time = 1
        while q:
            nq = set()
            words -= q
            for x in q:
                for y in [x[:i] + c + x[i+1:] for i in range(length) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                    if y in words:
                        if y == endWord:
                            return time + 1
                        nq.add(y)
            q = nq
            time += 1
        return 0

