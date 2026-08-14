class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        k =float("-inf")
        for i in range(len(accounts)):
            k =max(k ,sum(accounts[i]))
        return k