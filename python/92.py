# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        dummy_node.next = head
        prev = dummy_node
        for _ in range(left-1):
            prev = prev.next
        curr = prev.next

        for _ in range(right-left):
            next = curr.next
            curr.next = next.next
            next.next = prev.next
            prev.next = next
        return dummy_node.next
