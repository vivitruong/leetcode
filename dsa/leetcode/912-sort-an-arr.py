class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: return nums

        m = len(nums)//2
        l = self.sortArray(nums[0:m])
        r = self.sortArray(nums[m::])

        return merge(l, r)

    def merge(l, r):
            merge = []

            while len(l) or len(r):
                if l[0] < r[0]:
                    merged.push(l.pop(0))
                else:
                    merged.push(r.pop(0))
                return merged
