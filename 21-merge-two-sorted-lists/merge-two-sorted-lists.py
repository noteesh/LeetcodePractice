# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        l = ListNode()
        dummy = l

        while list1 and list2:
            if list1.val <= list2.val:
                l.next = list1
                list1 = list1.next
            else:
                l.next = list2
                list2 = list2.next
            l = l.next
        
        if not list1 and list2:
            l.next = list2
        elif not list2 and list1:
            l.next = list1

        return dummy.next