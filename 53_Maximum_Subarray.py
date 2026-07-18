class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i =0
        sum =0
        tsum =float("-inf")
        for i in range (0 ,len(nums)):
            sum =sum +nums[i]
            tsum =max(tsum ,sum)
            if sum <0:
                sum =0
        return tsum