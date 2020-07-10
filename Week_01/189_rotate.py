from  typing import  List

# 方法一，每次只挪动一位，重复k次
# O(n*k)
# 只需要一个常量保存最后一个数组值，空间复杂度O(1)

class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        for i in range(k):
            self.moveone(nums)

    def moveone(self,nums: List[int]):
        last = nums[-1]
        ln = len(nums)
        for i in range(ln):
            j = ln - i - 1
            if j > 0:
                nums[j] = nums[j-1]
        nums[0] = last


#方法2，学习了一种巧妙的反转方法，将nums反转，然后将nums[:k]反转，再将nums[k:]反转
#就是移动k的结果
# 时间复杂度O(n)，只需要反转3次，执行次数是n/2 + k/2 + (n-k)/2 = n
# 空间复杂度O(1)
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        nums.reverse()
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)

    def reverse(self, nums:List[int],i,k):
        while i <= k:
            nums[i], nums[k] = nums[k], nums[i]
            i += 1
            k -= 1