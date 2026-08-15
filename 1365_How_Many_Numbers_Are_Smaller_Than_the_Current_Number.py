class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans =[0]*len(nums)
        i =0
        for num in nums:
            count =0
            for n in nums:
                if num > n:
                    count+=1
            ans[i]=count
            i+=1
        return ans