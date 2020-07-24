from collections import deque

# 方法一，国际站上的高票python答案，学习了。思路很简单，对于每个节点，找它的左右节点，都有的话这个节点就是结果
class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(node,p,q):
            if not node: return None
            if node == p:
                return p
            elif node == q:
                return q
            leftNode = search(node.left,p,q)
            rightNode = search(node.right,p,q)

            if leftNode and rightNode:
                return node
            return leftNode or rightNode
        return search(root,p,q)


# 方法二，官方题解，存储每个节点的父亲节点，然后迭代找到公共的父亲节点
class Solution2:
    def __init__(self):
        self.father = {}
        self.seen = set()
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:return
            q = deque()
            q.append(root)
            while q:
                node = q.popleft()
                if node.left:
                    self.father[node.left.val] = node
                    dfs(node.left)
                if node.right:
                    self.father[node.right.val] = node
                    dfs(node.right)
        dfs(root)
        while p:
            self.seen.add(p.val)
            if p.val in self.father:
                p = self.father[p.val]
            else:
                break
        while q:
            if q.val in self.seen:
                return q
            q = self.father[q.val]
        return None

# 方法三，官方题解，思路其实和方法一很像，dfs遍历，如果左子树和右子树dfs都是true，或者是当前节点是p或者q，而且dfs有一个是true，
# 则该节点就是结果

class Solution3:
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node,p,q):
            if not node:return False
            lson = dfs(node.left,p,q)
            rson = dfs(node.right,p,q)
            if (lson and rson) or ((node.val == p.val or node.val == q.val) and (lson or rson)):
                self.ans = node
            return lson or rson or (node.val == p.val or node.val == q.val)
        dfs(root,p,q)
        return self.ans