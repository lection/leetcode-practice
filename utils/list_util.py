class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list2linked(array):
    if not array:
        return None
    head = last = ListNode(0)
    for n in array:
        node = ListNode(n)
        last.next = node
        last = node
    return head.next

def linked2list(head):
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result
