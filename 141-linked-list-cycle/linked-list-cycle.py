# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        p1 = head
        p2 = head.next

        while p1 and p2:
            if p1 == p2:
                return True
            else:
                p1 = p1.next
                if p2.next:
                    p2 = p2.next.next
                else:
                    return False
        
        return False