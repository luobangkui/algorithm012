学习笔记

### 注意点
再次注意. 先和面试官确认题目的相关点

再次注意，要确认好题目和条件，写代码时候要先处理好边界值和特殊情况

再次注意，注意变量命名

递归的特殊情况，二分法和回溯。本质都是找重复的子问题。需要根据具体问题确认好参数和终止条件，然后多多练习

### 作业

[全排列](https://github.com/luobangkui/algorithm012/edit/master/Week_03/46_permute.py)

[全排列II](https://github.com/luobangkui/algorithm012/edit/master/Week_03/47_permuteUnique.py)

[组合](https://github.com/luobangkui/algorithm012/edit/master/Week_03/77_combine.py)

[从前序与中序遍历序列构造二叉树](https://github.com/luobangkui/algorithm012/edit/master/Week_03/105_buildTree.py)

[二叉树的最近公共祖先](https://github.com/luobangkui/algorithm012/edit/master/Week_03/236_lowestCommonAncestor.py)



### 一般泛型递归

```

def recursion(level,p1,p2):
    # 1.满足条件退出
    if level > Max:
        process_result
        return

    # 2.process
    process(level,data)

    # 3. drill down
    recursion(level+1)
    # 4. reverse the current level status id needed

```

### 二分法
```
def divide_conquer( problem, param1, param2):
    if problem is None:
        print_result
        return
    data = prepare_data(problem)
    subproblems = split_problem(problem,data)
    subresult1 = self.divide_conquer(subproblems[0], p1...)
    subresult2 = self.divide_conquer(subproblems[1], p1...)
    subresult3 = self.divide_conquer(subproblems[2], p1...)
    ...
    result = process_result(subresult1,subresult2,subresult3, ...)
```
