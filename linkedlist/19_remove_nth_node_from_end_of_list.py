
#Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        curr=head
        while curr:
            l+=1
            curr=curr.next
        l-=n
        if l==0:
            return head.next
        curr=head
        for i in range(l-1):
            curr=curr.next
        curr.next=curr.next.next
        return head

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Input: head = [1], n = 1
# Output: []
