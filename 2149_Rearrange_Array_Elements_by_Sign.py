class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        k =0
        j =1
        result =[0]*len(nums)
        for num in nums:
            if num >0:
                result[k] =num
                k+=2
            if num < 0:
                result[j] =num
                j+=2
        return result