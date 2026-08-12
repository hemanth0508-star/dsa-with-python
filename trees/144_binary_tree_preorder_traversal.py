# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=list1
        l2=list2
        l3=ListNode('h')
        curr1=l1
        curr2=l2
        curr3=l3
        while curr1 and curr2:
            if curr1.val<=curr2.val:
                curr3.next=curr1
                curr1=curr1.next
                curr3=curr3.next
            else:
                curr3.next=curr2
                curr2=curr2.next
                curr3=curr3.next
        if curr1:
            curr3.next=curr1
        if curr2:
            curr3.next=curr2
        return l3.next        
