# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, tail):
        prev = None
        curr = head
        while prev != tail:
            node = curr.next
            curr.next = prev
            prev = curr 
            curr = node
        return tail, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        dummy_node.next = head
        
        prev = dummy_node
        while head:
            tail = prev
            for _ in range(k):
                tail = tail.next
                if tail == None:
                    return dummy_node.next
            node = tail.next
            head, tail = self.reverse(head, tail)
            prev.next = head
            tail.next = node
            prev = tail
            head = node

        return dummy_node.next
