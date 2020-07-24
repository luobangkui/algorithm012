from typing import List

# 第一遍看题，完全木有任何思路，回溯方法感觉不是太好理解，还是得自己多写几遍找感觉
# 第一个方法就是回溯法，时间复杂度是 kC(k,n) 前面k是把元素加到数组里，后面是组合个数
# 空间复杂度C(k,n)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(first, cur=[]):
            if len(cur) == k:
                res.append(cur[:])
                #res.append(cur)
                return
            for i in range(first,n+1):
                cur.append(i)
                backtrack(i+1,cur)
                # backtrack
                cur.pop()
        backtrack(1)
        return res


# 方法二，使用字典序的方法，实在是看不懂，还是多写几遍吧
class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1,k+1)) + [n+1]
        output ,j = [],0
        while j < k:
            output.append(nums[:k])
            j = 0
            print(' inner while')
            while j < k and nums[j+1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
                print(nums,j)
            nums[j] += 1
            print('outer while',nums)
        return output