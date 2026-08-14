class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxval =max(candies)
        ans =[0] * len(candies)
        i=0
        for num in candies:
            if num + extraCandies >= maxval:
                ans[i]=True
            else:
                ans[i]=False
            i+=1
        return ans
