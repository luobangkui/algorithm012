from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergesort(a, l, r):
            if r <= l:
                return 0
            mid = (l + r) >> 1
            count = mergesort(a, l, mid) + mergesort(a, mid+1, r)
            j = mid+1
            for i in range(l, mid+1):
                # while a[i] / 2.0 > a[j]:
                while j <= r and a[i]/2.0 > a[j]:
                    j += 1
                count += j - (mid+1)
            a[l:r+1] = sorted(a[l:r+1])
            return count
        return mergesort(nums, 0, len(nums)-1)