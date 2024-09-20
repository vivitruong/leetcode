# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.



# Example 1:

# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
# Example 2:

# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num+1):
            if i * i == num:
                return True
            if i* i > num:
                return False


#  var isPerfectSquare = function(num) {
#     let left = 1, right = num;

#     while(left <= right) {
#         let mid = Math.floor((left + right) / 2);

#         if(mid*mid === num) return true;
#         else if(mid*mid > num) right = mid -1;
#         else left = mid + 1;
#     }

#     return false;
# };
