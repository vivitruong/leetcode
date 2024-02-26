class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lis = {}
        ans = []
        for x in nums:
            if x in lis:
                lis[x] += 1
            else:
                lis[x] = 1
        sortList = sorted(lis.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            ans.append(sortList[i][0])
        return ans


#     Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
