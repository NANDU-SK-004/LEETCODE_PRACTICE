class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        l =[]
        while left < right:
            if numbers[right] > target :
                right -=1
            if (numbers[left] + numbers[right]) == target:
                l.append(left)
                l.append(right)
                return l
            elif (numbers[left] + numbers[right]) < target:
                left +=1
            else:
                right -=1