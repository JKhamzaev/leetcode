# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        if not head.next:
            return head
        
        pre_pre_cur = None
        pre_cur = head
        
        cur = head.next
        
        while cur:
            pre_cur.next = pre_pre_cur

            pre_pre_cur = pre_cur
            pre_cur = cur
            cur = cur.next
        
        pre_cur.next = pre_pre_cur



        return pre_cur

 