# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right or right < left:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        current, previous = head, dummy

        for i in range(1, right + 1):

            if i == left:
                left_bound = previous
                start_node = current

            if i == right:
                right_bound = current.next
                end_node = current

            previous = current
            current = current.next

        previous = start_node
        current = start_node.next

        while current != right_bound:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        start_node.next = right_bound
        left_bound.next = end_node

        return dummy.next