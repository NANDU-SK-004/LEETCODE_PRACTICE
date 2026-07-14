class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final =[]
        subset =[]
        candidates.sort()

        def solve(index ,subset ,target):
            if target == 0:
                return
            if index == len(candidates) or target <0:
                return
            for i in range(index ,len(candidates)):
                if candidates[i] == candidates[i-1] and i > index:
                    continue
                if candidates[i] >target:
                    break
                subset.append(candidates[i])
                solve(i+1 ,subset ,target -candidates[i])
                subset.pop()
        solve(0 , subset ,target)
        return final
        
        
        # final =[]
        # subset =[]
        # candidates.sort()

        # def dfs(index ,subset ,target):
        #     if target ==0:
        #         final.append(subset.copy())
        #         return
        #     if  target < 0 or index == len(candidates):
        #         return
        #     for i in range(index ,len(candidates)):
        #         if i > index and candidates[i] == candidates[i-1]:
        #             continue
        #         if candidates[i]> target:
        #             break
        #         subset.append(candidates[i])
        #         dfs(i +1 ,subset ,target - candidates[i] )
        #         subset.pop()
        #         # dfs(i-1 ,subset ,target + candidates[i])

        # dfs(0 ,subset ,target)
        
        # return final