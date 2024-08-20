# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.

# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0
        while l <=r:
            mid = (l+r)//2
            coins = (mid /2) * (mid+1)
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res)
        return res



#all javascript

# View on Github
# /**
#  * https://leetcode.com/problems/arranging-coins/
#  * Linear time
#  * Time O(n) | Space O(1)
#  * @param {number} n
#  * @return {number}
#  */
# var arrangeCoins = function(n) {

#     let steps = 1;
#     let canBuild = 0;

#     while(n >= steps) {
#         n = n - steps;
#         canBuild++;
#         steps++;
#     }

#     return canBuild || 1;
# };

# /**
#  * Binary Search
#  * Time O(log(n)) | Space O(1)
#  * @param {number} n
#  * @return {number}
#  */
# var arrangeCoins = function(n) {

#     let left = 1;
#     let right = n;
#     let result = 0;

#     while(left <= right) {

#         const mid = Math.floor((right+left)/2);
#         const total = (1 + mid) * (mid/2);
#         if(n < total) {
#             right = mid -1;
#         } else {
#             left = mid+1;
#             result = Math.max(result, mid);
#         }
#     }

#     return result;
#   };

# /**
#  * Math
#  * Time O(1) | Space O(1)
#  * @param {number} n
#  * @return {number}
#  */
# var arrangeCoins = function(n) {
#   let discriminant = 1 + 8 * n;
#   let sqrtDiscriminant = Math.sqrt(discriminant);

#   let result1 = Math.floor((-1 + sqrtDiscriminant) / 2);
#   let result2 = Math.floor((-1 - sqrtDiscriminant) / 2);

#   return Math.max(result1, result2);
# };
