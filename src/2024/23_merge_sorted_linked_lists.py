class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge2Lists(self, lists):
        out = dummy = ListNode(0)
        while lists[0] and lists[1]:
            if lists[0].val<lists[1].val:
                out.next = lists[0]
                
                lists[0] = lists[0].next
            else:
                out.next = lists[1]
                lists[1] = lists[1].next
            out = out.next
        if lists[0]:
            out.next = lists[0]
        if lists[1]:
            out.next = lists[1]
        return dummy.next

z=Solution()
a = ListNode(1,ListNode(5,None))
b = ListNode(2,ListNode(3,None))
b = ListNode(2,ListNode(3,None))
lists = [a, b]
out = z.merge2Lists(lists)
print(out.val, out.next.val, out.next.next.val)