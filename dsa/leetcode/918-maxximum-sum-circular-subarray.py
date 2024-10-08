# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.



# Example 1:

# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.
# Example 2:

# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
# Example 3:

# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for i, n in enumerate(nums):
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            globMax = max(curMax, globMax)
            globMin = min(curMin, globMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax


# var maxSubarraySumCircular = function (nums) {
#     let [globalMax, globalMin] = [nums[0], nums[0]];
#     let [currentMax, currentMin] = [0, 0];
#     let total = 0;

#     for (num of nums) {
#         currentMax = Math.max(num, currentMax + num);
#         currentMin = Math.min(num, currentMin + num);
#         total += num;
#         globalMax = Math.max(globalMax, currentMax);
#         globalMin = Math.min(globalMin, currentMin);
#     }

#     return globalMax > 0 ? Math.max(globalMax, total - globalMin) : globalMax;
# };


# class Solution {
#     public int maxSubarraySumCircular(int[] nums) {
#         int curMax = 0, curMin = 0;
#         int globMax = nums[0], globMin = nums[0];
#         int total = 0;
#         for (int n : nums) {
#             curMax = Math.max(curMax + n, n);
#             curMin = Math.min(curMin + n, n);
#             total += n;
#             globMax = Math.max(curMax, globMax);
#             globMin = Math.min(curMin, globMin);
#         }
#         return globMax > 0 ? Math.max(globMax, total - globMin) : globMax;
#     }
# }



#typescript
# View on Github
# function maxSubarraySumCircular(nums: number[]): number {
#     let [globalMax, globalMin] = [nums[0], nums[0]];
#     let [currentMax, currentMin] = [0, 0];
#     let total = 0;

#     for (let num of nums) {
#         currentMax = Math.max(num, currentMax + num);
#         currentMin = Math.min(num, currentMin + num);
#         total += num;
#         globalMax = Math.max(globalMax, currentMax);
#         globalMin = Math.min(globalMin, currentMin);
#     }

#     return globalMax > 0 ? Math.max(globalMax, total - globalMin) : globalMax;
# }


#i need to check agian because aparently i still dont understand
