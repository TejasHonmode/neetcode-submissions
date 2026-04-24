# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sj = head
        dj = head

        while dj and dj.next:
            sj = sj.next
            dj = dj.next.next
            if sj == dj:
                return True
        return False