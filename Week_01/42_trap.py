from typing import List

# 接雨水
# 使用双指针方法，分别从左右向中间遍历，途中每次遇到比当前maxh小的，sum加上对应差值，遇到更高的，更新对应的maxh
# 直到碰到所有柱子中最高的柱子。最后，计算最高柱子之间的sum

# 时间复杂度 O(n)，遍历整个数组需要n次
# 空间复杂度O(1)

class Solution1:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        lh = len(height)
        i,maxl = 0,height[0]
        j,maxr = lh-1,height[-1]
        maxh = max(height)
        sum = 0
        while height[i] < maxh:
            if i == 0:
                i += 1
                continue
            if height[i] >= maxl:
                maxl = height[i]
            else:
                sum += maxl - height[i]
            i += 1
        while height[j] < maxh:
            if j == lh-1:
                j -= 1
                continue
            if height[j] >= maxr:
                maxr = height[j]
            else:
                sum += maxr - height[j]
            j -= 1
        for k in range(i,j):
            sum += maxh - height[k]
        return sum

# 方法2看了高赞代码，使用一个栈做辅助
# 如果当前元素小于栈顶元素，入栈，否则出栈，并计算当前到左边界的水量
# 时间复杂度O(n)，因为只遍历了一次数组
# 空间复杂度O(n)，使用栈做辅助


class Solution2:
    def trap(self, height: List[int]) -> int:
        lh = len(height)
        if lh <= 1:
            return 0
        stack = []
        water = 0
        for i, h in enumerate(height):
            while stack and h >= stack[-1][1]:
                k = stack.pop()
                if stack:
                    # 注意栈和队列，别搞混了
                    # j, left_board = stack[0]
                    j, left_board = stack[-1]
                    # 这里为啥要用到i-j-1呢，因为leftboard是栈顶元素，是上一个左边界
                    # 相当于每次是从下往上计算水的量
                    water += (min(left_board, h) - k[1]) * (i - j - 1)
            stack.append((i, h))
        return water