"""
链表的插入排序
思路 边遍历 边倒序链表 最后再反转链表
=========
通过了 不过代码有点儿繁琐 反转似乎不够精炼
=========
网友居然用转成list再sort的方式 太不要脸了
=========
没精力折腾了 就先酱紫吧
=========
我特么是不是傻 何必反转两次呢 直接一次按从大到小就行了
"""
from utils import list_util


class Solution:
    def insertionSortList(self, head):
        if not head:
            return None
        # 遍历 反转 插入
        last = head
        cur = last.next
        last.next = None
        while cur is not None:
            cur_next = cur.next
            if cur.val <= last.val:
                cur.next = last
                last = cur
            else:
                temp = last
                temp_next = temp.next
                while temp_next is not None and temp_next.val < cur.val:
                    temp = temp_next
                    temp_next = temp.next
                cur.next = temp_next
                temp.next = cur
            cur = cur_next

        return last


s = Solution()
print(list_util.linked2list(s.insertionSortList(list_util.list2linked([4, 2, 1, 3]))) == [1, 2, 3, 4])
