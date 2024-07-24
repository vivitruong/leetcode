# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        right_pointer = head
        for _ in range(1, k):
            right_pointer = right_pointer.next
        left_kth_node = right_pointer

        left_pointer = head
        while right_pointer is not None:
            right_kth_node = left_pointer
            right_pointer = right_pointer.next
            left_pointer = left_pointer.next

        left_kth_node.val, right_kth_node.val = right_kth_node.val, left_kth_node.val
        return head
