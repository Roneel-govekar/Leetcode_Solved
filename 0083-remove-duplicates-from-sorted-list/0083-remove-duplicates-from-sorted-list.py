# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        list = head
        
        while(list.next!=None):
            if list.val == list.next.val:
                list.next = list.next.next
            else:
                list = list.next
        
        return head