class Solution:
    def combinationSum(self, candidates, target):
        final  = []
        sub = []
        candidates.sort()
        def solve(index ,sub ,target):
            i
            if target == 0:
                final.append(sub.copy())
                return
            
            
            for i in range(index ,len(candidates)):
                if candidates[i] > target :
                    break
                sub.append(candidates[i])  
                solve(i ,sub  ,target - candidates[i])   
            sub.pop()
        return final
        solve(0 ,sub ,target) 
        
        
        
        
                
        # final =[] 
        # subset =[]
        # candidates.sort()
        # def solve(index ,subset  ,target):

        #     if target == 0:
        #         final.append(subset.copy())
        #         return
            
        #     for i in range (index ,len(candidates)):
        #         if candidates[i] >target :
        #             break
        #         subset.append(candidates[i])
        #         sum =target-  candidates[i] 
        #         solve(i ,subset ,sum)
        #         subset.pop()
                
        # solve(0 ,subset,target)
        # return final

