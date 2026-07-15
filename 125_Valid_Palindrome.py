class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        l =[]
        while left < right:
            # if numbers[right] > target and numbers[right]+numbers[left]!= target:
            #     right -=1
            if (numbers[left] + numbers[right]) == target:
                l.append(left + 1)
                l.append(right + 1)
                return l
            elif (numbers[left] + numbers[right]) < target:
                left +=1
            else:
                right -=1