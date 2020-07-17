class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        path = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                path.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return path