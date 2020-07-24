
from  typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 第一遍自己做，花了比较长的时间，想到思路了，但是代码写的比较丑，而且还没通过。实际上找到了inorder.index(preorder[0]),就能
# 找到对应的左子树，和右子树的序列位置
class SolutionMyself:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: return None

        root = TreeNode(preorder[0])

        if preorder == inorder:
            root.right = self.buildTree(preorder[1:],inorder[1:])
            return root

        head = preorder[0]
        inhead = inorder.index(head)

        leftLast = inorder[inhead-1]

        leftPre = preorder[1:preorder.index(leftLast)+1]
        leftIno = inorder[:inhead]

        rightPre = preorder[preorder.index(leftLast)+1:]
        rightIno = inorder[inhead+1:]


        root.left = self.buildTree(leftPre, leftIno)
        root.right = self.buildTree(rightPre, rightIno)
        return root

# 又学习了高赞的代码
class SolutionTopvote:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:idx+1],inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:],inorder[idx+1:])
        return root