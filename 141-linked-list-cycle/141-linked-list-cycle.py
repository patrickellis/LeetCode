# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # to detect a cycle in a linked list
        # we can use a hare-and-tortoise algorithm:
        # two nodes progress through the list:
        # one at double the speed of the other
        # if at any point in time they land on the same
        # node, we know we have a cycle
        fast = slow = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if(fast == slow): return True
        return False