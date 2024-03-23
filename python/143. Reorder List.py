# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        while head.next!=None and head.next.next!=None:
            p = head
            while p.next.next != None:
                p = p.next
            p.next.next = head.next
            head.next = p.next
            p.next = None
            head = head.next.next
