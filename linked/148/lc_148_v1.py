"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

========
链表排序 用 归并排序 还不需要向数组那样申请额外的空间
难点是链表不像数组可以轻易的分成两部分 我琢磨琢磨
如果用快慢指针的方式 可以找到中间点 时间复杂度 n * log(n)
========
轻松通过 就是代码不够简洁
"""
from utils import list_util
from utils.list_util import ListNode


class Solution:
    def sortList(self, head):
        if not head:
            return None

        def rec(node):
            if node.next is None:
                return node
            mid = node
            fast = node
            while fast and fast.next:
                last = mid
                mid = mid.next
                fast = fast.next.next
            last.next = None
            n1 = rec(node)
            n2 = rec(mid)
            result = node = ListNode(0)
            while n1 and n2:
                if n1.val > n2.val:
                    n1, n2 = n2, n1
                node.next = n1
                node = node.next
                n1 = n1.next
            node.next = n2
            return result.next
        return rec(head)


s = Solution()
print(list_util.linked2list(s.sortList(list_util.list2linked([4, 2, 1, 3]))) == [1, 2, 3, 4])
