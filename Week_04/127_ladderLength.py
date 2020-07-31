from collections import defaultdict
from typing import List




# 前三遍都是按照下面的代码，偏背诵的方式做的。第四遍自己尝试去写，直接参考了126题，国际站高赞的答案
# 思路还是双向广度优先搜索，
# 首先得到所有combo下面的word的组合。
# 然后使用bq和eq两个字典来存当前的步数。 nq是用来每一层结束，更新下一次的bq
# bqseen和eqseen分别记录前后搜索的值
# 每次看完一层，交换bq和eq，同时交换eqseen和bqseen，

class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList:
            return 0
        all_combo, length = defaultdict(set), len(beginWord)
        for word in wordList:
            for i in range(length):
                all_combo[word[:i] + '_' + word[i+1:]].add(word)
        bq, eq, nq = {beginWord: 1}, {endWord: 1}, {}
        bqseen, eqseen = set(), set()
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

# 这道题目和基因序列题目比较类似，可以使用广度优先搜索，同时学习了一下双向广度优先搜索的写法
# 时间复杂度是O(M * N) M是单词长度，N是单词表单词数

class Solution1:
    def __init__(self):
        self.all_combo = defaultdict(list)
        self.length = 0

    def visitqueue(self, queue, visited, other_visited):
        cur, level = queue.pop(0)

        for i in range(self.length):
            s = cur[:i] + '*' + cur[i+1:]
            for word in self.all_combo[s]:
                if word in other_visited:
                    return level + other_visited[word]
                if word not in visited:
                    visited[word] = level + 1
                    queue.append([word, level + 1])
        return None


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord or not beginWord or not wordList or endWord not in wordList:
            return 0
        self.length = len(beginWord)
        for word in wordList:
            for i in range(self.length):
                self.all_combo[word[:i]+'*'+word[i+1:]].append(word)

        queue_begin = [(beginWord, 1)]
        queue_end = [(endWord, 1)]
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None

        while queue_begin and queue_end:
            ans = self.visitqueue(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            ans = self.visitqueue(queue_end, visited_end, visited_begin)
            if ans:
                return ans
        return 0