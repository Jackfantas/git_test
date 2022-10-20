class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reversed(head, n):
    if n==1:
        successor = head.next
        return head, successor
    new_head, successor = reversed(head.next, n-1)
    head.next.next = head
    head.next = successor
    return new_head