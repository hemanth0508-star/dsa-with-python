'''
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=0
        curr=head
        while curr:
            l+=1
            curr=curr.next
        a=(l//2)
        curr=head
        while curr and a>0:
            curr=curr.next
            a-=1
        head=curr
        return head
#code file
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
