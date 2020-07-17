# 后序遍历和前序遍历十分相似，后续遍历可以先遍历根节点，然后遍历孩子节点压栈，最后path正好是后续的逆序，所以直接取逆序返回

from typing import List
class Solution:
    def __init__(self):
        self.travel_path = []
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root,]
        while stack:
            root = stack.pop()
            if root:
                self.travel_path.append(root.val)
            for c in root.children:
                stack.append(c)
        self.travel_path = self.travel_path[::-1]
        return self.travel_path