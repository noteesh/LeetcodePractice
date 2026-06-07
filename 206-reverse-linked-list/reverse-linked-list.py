# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1 <- 2 <- 3

        prev = 3
        temp = None
        nextTemp = None
        '''

        if not head or (not head.next):
            return head
        
        prev = None
        temp = head
        while temp:
            nextTemp = temp.next
            temp.next = prev
            prev = temp
            temp = nextTemp
        
        return prev



