# Given the head of a linked list, return the list after sorting it in ascending order.
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.get_mid(head)
        left, right = self.sortList(head), self.sortList(mid)

        return self.merge_two_sorted(left, right)


    def merge_two_sorted(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        sentinel = ListNode()
        prev = sentinel
        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        if list1:
            prev.next = list1
        else:
            prev.next = list2

        return sentinel.next


    def get_mid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid_prev = None
        while head and head.next:
            mid_prev = mid_prev.next if mid_prev else head
            head = head.next.next

        mid = mid_prev.next
        mid_prev.next = None

        return mid

        #javasoluition
# class Solution {
#     // Merge Sort Implementation
#     public ListNode getMid(ListNode head){
#         ListNode slow=head, fast=head.next;
#         while(fast != null && fast.next != null){
#             fast = fast.next.next;
#             slow = slow.next;
#         }
#         return slow;
#     }
#     public ListNode merge(ListNode left, ListNode right){
#         ListNode dummy = new ListNode();
#         ListNode tail = dummy;

#         while(left != null && right != null){
#             if(left.val < right.val){
#                 tail.next = left;
#                 left = left.next;
#             }else{
#                 tail.next = right;
#                 right = right.next;
#             }
#             tail = tail.next;
#         }
#         if(left != null){
#             tail.next = left;
#         }
#         if(right != null){
#             tail.next = right;
#         }
#         return dummy.next;
#     }
#     public ListNode sortList(ListNode head) {
#         if(head == null || head.next == null){
#             return head;
#         }

#         // Split the list in 2 halfs
#         ListNode left = head;
#         ListNode right = getMid(head);
#         ListNode tmp = right.next;
#         right.next = null;
#         right = tmp;

#         left = sortList(left);
#         right = sortList(right);
#         return merge(left, right);
#     }
# }

# // Using a Heap to sort the list
# class Solution {
#     public ListNode sortList(ListNode head) {
#         if(head == null || head.next == null){
#             return head;
#         }
#         PriorityQueue<Integer> queue = new PriorityQueue<>();
#         ListNode temp = head;
#         while(temp.next!=null){
#             queue.add(temp.val);
#             temp = temp.next;
#         }
#         queue.add(temp.val);
#         temp = head;
#         while(!queue.isEmpty()){
#             temp.val = queue.poll();
#             temp = temp.next;
#         }
#         return head;
#     }
# }
