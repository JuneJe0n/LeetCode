class ListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        # Dummy node (head, tail 요구하는 함수 있으니까 둘다 init)
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1


    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node

        if not node.next:
            self.tail = node


    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        # move until prev
        while i < index and curr: # [edge: oob] and curr
            i += 1
            curr = curr.next

        if curr and curr.next: # [edge: oob]
            # [edge] if remove tail
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True

        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
            










