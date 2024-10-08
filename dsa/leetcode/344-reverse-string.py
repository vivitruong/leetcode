# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.



# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l < r:
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1



#  var reverseString = function(s) {
#     let i = 0, j = s.length-1;

#     while(i <= j) {
#         let leftval = s[i], rightval = s[j];
#         s[i] = rightval;
#         s[j] = leftval;

#         i++;
#         j--;
#     }
# };

#typescript
# function reverseString(s: string[]): void {
#     let l = 0;
#     let r = s.length - 1;

#     while (l < r) {
#         let temp = s[l];
#         s[l] = s[r];
#         s[r] = temp;
#         l += 1;
#         r -= 1;
#     }
# }



#java
# class Solution {
#     public void reverseString(char[] s) {
#         //Do not return anything, modify s in-place instead.
#         int l = 0;
#         int r = s.length - 1;
#         while(l <= r) {
#             char tmp = s[l];
#             s[l++] = s[r];
#             s[r--] = tmp;
#         }
#     }
# }
