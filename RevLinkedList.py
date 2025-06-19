from typing import Optional
# list_node.py
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

def build_linked_list(vals: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next  

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr= None, head
        while(curr):
            temp = curr.next
            curr.next =prev
            prev = curr
            curr = temp
        return prev

if __name__ =='__main__':
    head = [0,1,2,3]
    sil = Solution()
    head = build_linked_list(head)
    print(sil.reverseList(head))