# T O(n) M O(1)

class ListNode():
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use 2 ptrs
        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
