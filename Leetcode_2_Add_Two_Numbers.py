# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        root = head
        carry = 0

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + carry

            carry = s // 10
            head.next = ListNode(s % 10)
            head = head.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if carry:
            head.next = ListNode(carry)

        return root.next


'''
  T = O(max(M,N))
  S = O(max(M,N))
'''
