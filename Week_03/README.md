学习笔记

###
再次注意. 先和面试官确认题目的相关点
再次注意，要确认好题目和条件，写代码时候要先处理好边界值和特殊情况
再次注意，注意变量命名
###


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