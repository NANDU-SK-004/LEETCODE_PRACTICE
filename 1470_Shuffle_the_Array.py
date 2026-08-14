class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        k =1
        for i in range (n ,len(nums)):
            nums.insert(k,nums[i])
            k+=1
        return nums