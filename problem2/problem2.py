# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    sval = l1.val + l2.val
    if sval < 10:
        result = ListNode(sval)
        result.next = addTwoNumbers(l1.next, l2.next)
        return result
    else: # carry the 1
        result = ListNode(sval - 10)
        result.next = addTwoNumbers(ListNode(1), addTwoNumbers(l1.next, l2.next))
        return result