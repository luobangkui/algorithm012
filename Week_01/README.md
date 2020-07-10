
### 学习心得

#### lesson one

第一课还是学到了很多东西，明白了自己的很多误区的地方。

话说自己大学四年一直是一个菜鸡的角色，身边不乏各种计算机大佬大神。和大佬的距离越来越大，慢慢自己也慢慢丧失了信心和动力。感觉现在才明白自己和大佬差在哪里----懒惰，除了行动上的，更重要的是思想上的懒惰。这一课提到的误区，感觉自己从小学到现在都没有改过，那就是超哥提到的死磕到底，我到现在才知道这是不对的，比如做算法题，花了一天去想去做才做出来，从头到尾就做了一遍，跟超哥讲的东西完全背道而驰。

所以我自己准备按照超哥的思路和方法，重新学一次算法和数据结构，把自己当成一个初学者。回头再来检验一下自己的实践成果。

#### lesson two

我把5遍刷题列到了mac的提醒事项里。每次做完更新一下时间和次数，我觉得这种方法还不错，就是可能后面todo list会越堆越多

视频练了第一遍和第二遍，关于数组的相关题目。都是第一遍看题目完全没思路。看完题解之后，还是有很多细节,和边界值，数组下标相关的地方没注意到，导致ac失败。而且有一些地方自己可能也没太理解。比如，盛最多水容器这道题，i++和j--，我把java的代码翻版到python里又不对了。

把一些做题容易错的地方，和需要注意的地方记录到了云笔记上面
##### 数组 http://note.youdao.com/s/VKbThZ1J
##### 栈和队列 http://note.youdao.com/s/YN7xVK1d


### 分析 queue和priority queue的源码

python 的deque是c语言模块提供的实现的内建模块

python 的优先级队列是heapq模块里实现的，内部使用了堆的结构
heapq提供了如下的方法

```
__all__ = ['heappush', 'heappop', 'heapify', 'heapreplace', 'merge',
           'nlargest', 'nsmallest', 'heappushpop']
```

简单看一下入队列和出队列

```
def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)
```

入队列操作```heappush```，会向heap里面push进去一个元素，然后调用_siftdown，去调整堆。

```
def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem
```

_siftdown方法，会对堆进行调整，把pos位置的元素放到堆的对应位置。


```
def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt
```
出队列```heappop```操作，第一行```lastelt = heap.pop() ```的目的是为了空队列情况下系统跑出异常。因为堆顶是最小的元素，所以直接弹出堆顶。然后调用```_siftup```来调整堆

```
def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)
```
```_siftup```  把元素放到所属的位置上，然后调用```_siftdown```调整它的父亲，重新满足二叉树堆

由于堆的插入和删除操作时间复杂度都是O(logn)，所以优先级队列的push和pop的时间复杂度是O(logn)