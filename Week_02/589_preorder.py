
# 前序遍历和后续遍历其实是有相反的，所以可以把前序和后续用类似的方式压入栈中,
# 前序先遍历root，然后孩子节点压栈顺序和输出顺序相反。也就是先把右边的孩子压入栈
from typing import List
class Solution:
    def __init__(self):
        self.path = []
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root,]
        while stack:
            root = stack.pop()
            self.path.append(root.val)
            for i in root.children[::-1]:
                stack.append(i)
        return self.path