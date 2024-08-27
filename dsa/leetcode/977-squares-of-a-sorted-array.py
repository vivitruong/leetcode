# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1

        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                res[r - l] = left * left
                l += 1
            else:
                res[r - l] = right * right
                r -= 1
        return res


# var sortedSquares = function (nums) {
#     let left = 0;
#     let right = nums.length - 1;

#     const answer = [];

#     while (left <= right) {
#         const leftSqr = Math.pow(nums[left], 2);
#         const rightSqr = Math.pow(nums[right], 2);

#         if (leftSqr > rightSqr) {
#             answer.push(leftSqr);
#             left++;
#         } else {
#             answer.push(rightSqr);
#             right--;
#         }
#     }
#     return answer.reverse();
# };
