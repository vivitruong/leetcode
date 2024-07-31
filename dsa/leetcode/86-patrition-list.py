# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head, bigger_head = ListNode(-1), ListNode(-1)
        less_prev, bigger_prev = less_head, bigger_head
        while head:
            if head.val < x:
                less_prev.next = head
                less_prev = less_prev.next
            else:
                bigger_prev.next = head
                bigger_prev = bigger_prev.next

            head = head.next

        less_prev.next = bigger_prev.next = None
        less_prev.next = bigger_head.next

        return less_head.next
