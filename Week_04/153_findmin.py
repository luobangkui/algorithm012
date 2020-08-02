from  typing import List
# 思路和搜索旋转排序数组一样看左右是否有序，左边有序找右边。右边有序找左边。
# 需要注意一点是，二分法查找找的是一个数，但是这个题目需要看两个数，所以nums[mid] < nums[mid-1] 和 nums[mid] > nums[mid+1]
# 都需要处理一下。
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:return -1
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)//2
            if mid > 0 and nums[mid] < nums[mid-1]:
                return nums[mid]
            if mid < n-1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # 如果左边有序,找右边
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[0]

