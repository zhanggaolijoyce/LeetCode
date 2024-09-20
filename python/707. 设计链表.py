class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        node = self.head 
        for _ in range(index+1):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
        elif index > self.size:
            return
        else:
            node = self.head
            for _ in range(index):
                node = node.next
            node1 = node.next
            node.next = ListNode(val)
            node.next.next = node1
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        node = self.head
        for _ in range(index):
            node = node.next
        node.next = node.next.next
        self.size -= 1
