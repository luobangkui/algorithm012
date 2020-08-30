## 学习笔记


### 作业
[N皇后](https://github.com/luobangkui/algorithm012/blob/master/Week_08/51_solveNQueens.py)

[N皇后II](https://github.com/luobangkui/algorithm012/blob/master/Week_08/52_totalNQueens.py)

[区间合并](https://github.com/luobangkui/algorithm012/blob/master/Week_08/56_merge.py)

[LRU缓存](https://github.com/luobangkui/algorithm012/blob/master/Week_08/146_lrucache.py)

[颠倒二进制位](https://github.com/luobangkui/algorithm012/blob/master/Week_08/190_reverseBits.py)

[位1的个数](https://github.com/luobangkui/algorithm012/blob/master/Week_08/191_hammingWeight.py)

[2的幂](https://github.com/luobangkui/algorithm012/blob/master/Week_08/231_isPowerOfTwo.py)

[有效的字母异位词](https://github.com/luobangkui/algorithm012/blob/master/Week_08/242_isAnagram.py)

[翻转对(注意统计count j的下标不要越界)](https://github.com/luobangkui/algorithm012/blob/master/Week_08/493_reversePairs.py)

[数组的相对排序](https://github.com/luobangkui/algorithm012/blob/master/Week_08/1112_relativeSortArray.py)


### 基础排序--选择排序
```
def selectsort(array):
    tmp = []
    for i in range(len(array)):
        minval = min(array)
        tmp.append(minval)
        array.remove(minval)
    array[:] = tmp
```
### 基础排序--插入排序
```
def insertsort(array):
    length = len(array)
    for i in range(1, length):
        preidx = i-1
        current = array[i]
        while preidx >= 0 and array[preidx] > current:
            array[preidx+1] = array[preidx]
            preidx -= 1
        array[preidx+1] = current
```

### 基础排序--冒泡排序
```
def bubblesort(array):
    length = len(array)
    for i in range(length-1, -1, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
```





### 高级排序--快排
```
def partition(array, begin, end):
    counter, pivot = begin, end
    for i in range(begin, end):
        if array[i] < array[pivot]:
            array[i], array[counter] = array[counter], array[i]
            counter += 1
    array[counter], array[pivot] = array[pivot], array[counter]
    return counter

def quicksort(array, begin, end):
    if end <= begin:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot - 1)
    quicksort(array, pivot + 1, end)

```

### 高级排序--归并排序

```
def merge(array, left, mid, right):
    temp = []
    i, j = left, mid+1
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1

    while i <= mid:
        temp.append(array[i])
        i += 1

    while j <= right:
        temp.append(array[j])
        j += 1

    array[left:right+1] = temp

def mergesort(array, left, right):
    if right <= left:
        return
    mid = (left + right) >> 1
    mergesort(array, left, mid)
    mergesort(array, mid+1, right)
    merge(array, left, mid, right)
```

