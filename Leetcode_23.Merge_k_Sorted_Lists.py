import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap =[]
        head = ListNode(-1)
        root= head
        
        for idx, element in enumerate(lists):
            if element:
                heapq.heappush(heap, (element.val, idx, element))
                
        while heap:
            val, idx, node = heapq.heappop(heap)
            
            head.next = ListNode(val)
            head = head.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
                
        return root.next
           
