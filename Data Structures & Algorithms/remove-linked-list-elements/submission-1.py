# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head:
            return head
        
        if head.val == val and head.next is None:
            del head
            head = None
            return head

        
        dummy = ListNode(-1)
        dummy.next = head
        current = head
        previous = dummy
        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = current
            
            current = current.next
        
        return dummy.next
