# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # to reverse a list:
        # three variables:
        # prev, curr, next
        # curr = head
        # curr = curr->next
        # head->next = prev
        # prev = head
        
        prev, curr = None, head
        while(curr):
            head = head.next
            curr.next = prev
            prev = curr
            curr = head
        return prev
            