# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and list2:
            return list2

        if list1 and not list2:
            return list1
        
        
        cur1 = list1
        cur2 = list2
        ans = ListNode()
        answer = ans
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                answer.next = cur1
                cur1 = cur1.next
            else:
                answer.next = cur2
                cur2 = cur2.next
            answer = answer.next

        if cur1:
            answer.next = cur1
        else:
            answer.next = cur2

        return ans.next
