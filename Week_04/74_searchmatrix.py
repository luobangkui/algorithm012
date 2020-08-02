from  typing import List

#用二分法
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:return False
        m, n = len(matrix), len(matrix[0])
        l1, r1 = 0, m-1
        l2, r2 = 0, n-1
        m1, m2 = 0, 0
        while l1 <= r1:
            m1 = (l1 + r1)//2
            if target >= matrix[m1][0] and target <= matrix[m1][-1]:
                break
            elif target < matrix[m1][0]:
                r1 = m1 - 1
            else:
                l1 = m1 + 1
        while l2 <= r2:
            m2 = (l2 + r2)//2
            if matrix[m1][m2] == target:
                return True
            elif target > matrix[m1][m2]:
                l2 = m2 + 1
            else:
                r2 = m2 - 1
        return False

# 方法二，直接一次二分法， 直接整个看错一个整体进行二分。判断matrix[mid//n][mid%n]和target关系，n是数组里数组的长
class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:return False
        # m, n = len(matrix)-1, len(matrix[0])-1
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        while l <= r:
            mid = (l+r)//2
            # if matrix[mid//n][mid%m] == target:
            #     return True
            if matrix[mid//n][mid%n] < target:
                l = mid + 1
            elif matrix[mid//n][mid%n] > target:
                r = mid - 1
            else:
                return True
        return False