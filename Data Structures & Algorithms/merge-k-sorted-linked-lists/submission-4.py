# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next


        # if not lists:
        #     return None

        # res = ListNode(0)
        # cur = res

        # while True:
        #     min_node = -1
        #     for i in range(len(lists)):
        #         if not lists[i]:
        #             continue
        #         if min_node == -1 or lists[i].val < lists[min_node].val:
        #             min_node = i
            
        #     if min_node == -1:
        #         break
            
        #     cur.next = lists[min_node]
        #     lists[min_node]  = lists[min_node].next
        #     cur = cur.next

        # return res.next 


