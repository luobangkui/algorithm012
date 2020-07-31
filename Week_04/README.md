学习笔记


### 作业

[跳数](https://github.com/luobangkui/algorithm012/edit/master/Week_04/55_canjump.py)

[平方根](https://github.com/luobangkui/algorithm012/edit/master/Week_04/69_mysqrt.py)

[股票最大收益](https://github.com/luobangkui/algorithm012/edit/master/Week_04/122_maxprofit.py)

[单词接龙I](https://github.com/luobangkui/algorithm012/edit/master/Week_04/127_ladderLength.py)

[单词接龙II](https://github.com/luobangkui/algorithm012/edit/master/Week_04/126_findLadders.py)

[岛屿数量](https://github.com/luobangkui/algorithm012/edit/master/Week_04/200_numIslands.py)

[分饼干](https://github.com/luobangkui/algorithm012/edit/master/Week_04/455_findcontentChildren.py)

题目还是过遍数，尤其是单词接龙的题目，看完高赞答案，直接学过来写，主要思想利用双向广度优先搜索。

双向广度优先搜索，通常使用一个beginqueue, endqueue, begvisited, endvisited。
然后双向向中间层层迭代，直到结果相交。

贪心算法：局部最优值累计得到结果最优。和动态规划区别在于，贪心算法不保存历史记录不能回退，没有回溯。而动态规划保存历史结果
难点在于，从什么点去切入找到局部最优。可能是从前，或者从中间，或者从后向前。



### 二分法（直接背下来）

```
left, right = 0, len(array) - 1
while left <= right:
    mid = (left + right)/2
    if array[mid] == target:
        # find target!
        return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```