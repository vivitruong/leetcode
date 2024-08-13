# You are given a string s, which contains stars *.

# In one operation, you can:

# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# Note:

# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.


# Example 1:

# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".
# Example 2:

# Input: s = "erase*****"
# Output: ""
# Explanation: The entire string is removed, so we return an empty string.
class Solution(object) :
    def removeStars(self, s) :
        res = []
        for c in s :
            if res and c == '*':
                res.pop()
            else:
                res.append(c)
        return ''.join(res)

#java
# class Solution {
#     public String removeStars(String s) {

#         // Create a new stack to keep track of characters encountered so far
#         Stack<Character> stk = new Stack<>();

#         // Iterate over each character in the input string
#         for (char c : s.toCharArray()) {
#             // If the current character is a star,
#             // remove the topmost character from the stack
#             if (c == '*') {
#                 stk.pop();
#             }
#             // If the current character is not a star, add it to the stack
#             else {
#                 stk.push(c);
#             }
#         }

#         // StringBuilder to store the characters in the stack
#         StringBuilder sb = new StringBuilder();
#         for (char c : stk) {
#             sb.append(c);
#         }

#         // Convert the StringBuilder to a string and return it as the output
#         return sb.toString();
#     }
# }
