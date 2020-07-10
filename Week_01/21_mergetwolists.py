#方法1 新建一个ListNode head, l1和l2节点逐次比较，向head里添加
#l1和l2长度m、n，时间复杂度是O(m+n)
#空间复杂度 是m+n

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        head = l1
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        res = head
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        while l1:
            head.next = l1
            l1 = l1.next
            head = head.next
        while l2:
            head.next = l2
            l2 = l2.next
            head = head.next
        return res


# 学习了一下方法2，使用递归的方式，if l1.val < l2.val，则对l1.next和l2进行merge，反之亦然
# 时机复杂度 递归的实际复杂度是  O(T) = R * O(s) R是递归次数，O(s) = 每次执行的时间复杂度
# 每次取下一个next，遍历了整个l1和l2，所以R = m + n , 每次执行O(s) = 1  O(T) = m + n
# 空间复杂度 是递归深度，也是O(m+n)
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
