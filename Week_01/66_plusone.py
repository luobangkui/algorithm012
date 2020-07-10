from typing import List


# 第一种方法，利用str和int类型转换，但是面试时候会让这么做？
# 时间复杂度O(n)，因为需要遍历元素进行转换
# 空间复杂度O(n)，新申请了res数组返回结果，
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        def join(digits: List[int]):
            s = ""
            for i in digits:
                s += str(i)
            return s
        s = join(digits)
        rs = int(s) + 1
        res = []
        for i in str(rs):
            res.append(int(i))
        return res

#方法2 从后向前，遍历进位，如果不需要进位直接返回结果
# 时间复杂度O(n)，最坏情况要遍历整个数组
# 空间复杂度O(1) 直接原地修改数组
# 看了别人的代码，发现自己多此一举写了一个进位标志，其实根本不需要看是否进位，因为不进位直接返回了
class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        ld = len(digits)
        isCarry = True
        for i in range(ld):
            j = ld -i - 1
            if isCarry:
                if digits[j] + 1 == 10:
                    isCarry = True
                    digits[j] = 0
                else:
                    digits[j] = digits[j] + 1
                    return digits
        if isCarry:
            return [1] + digits

class Solution2Opt:
    def plusOne(self, digits: List[int]) -> List[int]:
        ld = len(digits)
        for i in range(ld):
            j = ld -i - 1
            if digits[j] + 1 == 10:
                digits[j] = 0
            else:
                digits[j] = digits[j] + 1
                return digits
        return [1] + digits
