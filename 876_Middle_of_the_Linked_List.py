class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = head

        while curr and curr.next:
            prev = prev.next
            curr = curr.next.next

        return prev
        