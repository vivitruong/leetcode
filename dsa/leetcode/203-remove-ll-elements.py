# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.



# Example 1:


# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(next=head)
        prev, curr = dummy, head

        while curr:
            nxt = curr.next

            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr

            curr = nxt
        return dummy.next

# add dtypescreto[t]
# function removeElements(head: ListNode | null, val: number): ListNode | null {

#     let sentinel_node : ListNode = new ListNode(0, head);
#     let slow_pointer  : ListNode | null = sentinel_node;
#     let fast_pointer  : ListNode | null = null;

#     while (slow_pointer) {

#         // get next legible node
#         fast_pointer = slow_pointer.next;
#         while (fast_pointer && fast_pointer.val === val) {
#             fast_pointer = fast_pointer.next;
#         }

#         // Set next node to the legible node
#         slow_pointer.next = fast_pointer;
#         slow_pointer      = slow_pointer.next;
#     }

#     return sentinel_node.next;
# };
