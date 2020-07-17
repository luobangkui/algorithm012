学习笔记





本周完成了这周课程实战题目和作业题目的前三遍，以及上周题目的第四遍。

做题笔记：http://note.youdao.com/s/A47k3MDL

#### 关于堆
涉及到处理最大值或者最小值的时候，可以使用堆的数据结构

找k个最大/小元素，维护长度为k的小/大顶堆。原因是，比如找最小k个元素，大顶堆表示当前堆顶是最大值，如果来值的比最大值还小，就把最大值pop出去。最终结果就是
把所有比前k个最小元素大的元素全都pop出去，剩下的就是k个最小值元素。找k个最大值反之。

#### 关于树的遍历

树的前、中、后序遍历，都可以用简便的递归方式处理。

但是实际可能会问你迭代的方式，迭代的方式都是使用一个stack做辅助。前序和后序的处理方式比较类似。
前序，就是先输出root，再把孩子逆序遍历入栈。
后序，可以看做是前序的逆序，这里的前序，是根->右->左的顺序。
中序，需要迭代到最左边的子树，然后对应的元素入栈，再把right入栈。然后依次迭代

树的层次遍历，使用一个队列去做辅助，用bfs的方式去处理。

##### 先序
```
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
```

##### 后序
```
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
```

##### 中序
```
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        path = []
        if not root:return []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            path.append(cur.val)
            cur = cur.right
        return path
```

##### 层次遍历
```
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
```




