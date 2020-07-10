from  typing import  List

#最差只需要遍历一遍整个数组，所以时间复杂度是O(n)
#只使用了count临时遍历，空间复杂度O(1)

class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        for i in range(len(nums)):
            if i == 0:
                continue
            if nums[i] != nums[i-1]:
                count += 1
                nums[count] = nums[i]
        return count + 1


#每次从后向前遍历，如果遇到重复的项，则删掉重复项，直到计数器count == len(nums) 为止，返回count计数
#时间复杂度分析，假如长度是n，每个元素重复k次， 则遍历到一个不重复元素，需要删除k-1个元素，
#元素移动次数是（1+2+..+(n-n/k)) T =  1+2+..+(n-n/k) 也就是O(n^2）的时间复杂度
#空间复杂度O(1)


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln <= 1:
            return ln
        count = 1
        while True:
            if nums[-count] == nums[-count-1]:
                nums.pop(-count)
            else:
                count += 1
            if count == len(nums):
                return count