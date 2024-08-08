# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

#  Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:

# Input: head = []
# Output: []
# Example 3:

# Input: head = [1]
# Output: [1]
#medium

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # save ptrs
            nxtPair = curr.next.next
            second = curr.next

            # reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second

            # update ptrs
            prev = curr
            curr = nxtPair

        return dummy.next
