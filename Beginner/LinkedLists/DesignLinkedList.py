class ListNode:
    def __init__(self, val = None, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: # [oob]
            return -1
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        next_node = self.head.next

        # link w next node
        new_node.next = next_node
        next_node.prev = new_node

        # link w head
        self.head.next = new_node
        new_node.prev = self.head

        self.size += 1


    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        prev_node = self.tail.prev

        # link w tail
        new_node.next = self.tail
        self.tail.prev = new_node

        # link w prev node
        prev_node.next = new_node
        new_node.prev = prev_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # oob using size
        if index < 0 or index > self.size:
            return 
        
        # go to prev
        new_node = ListNode(val)
        curr = self.head

        for _ in range(index):
            curr = curr.next
        next_node = curr.next

        # add at index
        new_node.next = next_node
        next_node.prev = new_node

        curr.next = new_node
        new_node.prev = curr

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # check oob
        if index < 0 or index >= self.size:
            return 

        # go to prev
        curr = self.head
        for _ in range(index):
            curr = curr.next
        next_node = curr.next.next

        # remove
        curr.next = next_node
        next_node.prev = curr

        self.size -= 1









