class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = float("+inf")
        max_doff =float("-inf")
        for i in range(0 ,len(prices)):
            least = min(least ,prices[i])
            max_doff =max(max_doff ,prices[i] - least)
        return max_doff
