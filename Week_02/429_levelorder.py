
from  typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# 方法一，每次把上一层的所有孩子节点存到数组里，直到新的一层没有节点
class Solution1:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:return []
        res = [[root]]
        nres = [[root.val]]
        level = 0
        tmp = [root.val]
        while tmp:
            tmp = []
            tmpr = []
            for r in res[level]:
                for c in r.children:
                    tmp.append(c)
                    tmpr.append(c.val)
            if tmp:
                res.append(tmp)
                nres.append(tmpr)
                level += 1
        return nres

# 方法二，广度优先搜索，时间复杂度O(n)， 空间复杂度O(n)
from  collections import deque
class Solution2:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:return []
        queue = deque([root])
        res = []
        while queue:
            tmp = []
            for _ in range(len(queue)):
                left = queue.popleft()
                tmp.append(left.val)
                queue.extend(left.children)
            res.append(tmp)
        return res