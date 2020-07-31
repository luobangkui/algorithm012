from collections import defaultdict
from  typing import List


# 直接嫖了国际站的高票答案，第二遍基本背着写下来了，顺便学习了人家的思路和写法
# 时间复杂度M ^ 26
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not beginWord or not endWord or not wordList or not endWord in wordList:
            return []
        bq, eq, nq, rev, tree = {beginWord}, {endWord}, set(), False, defaultdict(set)
        length, words, found = len(beginWord), set(wordList), False
        while bq and not found:
            words -= bq # set操作学到了，words 去掉已经找过的单词， 如果在下面for里面调用words.remove会出错。
            for x in bq:
                for i in range(length):
                    for y in [x[:i] + c + x[i+1:] for c in 'qwertyuiopasdfghjklzxcvbnm']:
                        if y in words:
                            if y in eq:
                                found = True
                            else:
                                nq.add(y)
                            tree[x].add(y) if not rev else tree[y].add(x)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq, rev = eq, bq, not rev
        # 把单词的下一步直接，存到tree里面了，直接递归找出对应的路径
        def bt(x):
            # 第二遍这里错了，是把x加到当前结果里，y是它的下一层的单词
            return [[x]] if x == endWord else [[y] + rest for y in tree[x] for rest in bt(y)]
            # return [[x]] if x == endWord else [[y] + rest for y in tree[x] for rest in bt(y)]
        return bt(beginWord)
