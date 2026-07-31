from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def solve(index, total, bracket, result):
            if index >= len(bracket):
                if total == 0:
                    result.append("".join(bracket))
                return

            # Pruning
            if total > len(bracket) // 2:
                return
            if total < 0:
                return

            # Place '('
            bracket[index] = "("
            balance = total + 1
            solve(index + 1, balance, bracket, result)

            # Place ')'
            bracket[index] = ")"
            balance = total - 1
            solve(index + 1, balance, bracket, result)

        bracket = [""] * (2 * n)
        result = []
        solve(0, 0, bracket, result)
        return result


# Driver
obj = Solution()
print(obj.generateParenthesis(3))