class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1 =list(set(nums1))
        num2 =list(set(nums2))
        i ,j =0 ,0
        while i < len(num1) and j < len(num2):
            if num1[i] == num2[j]:
                i+=1
                j+=1
            elif num1[i] < num2[j]:
                i+=1
            else:
                num1.insert(i ,num2[j])
                j+=1
        if j < len(num2):
                num1.append(num2[j:len(num2)])
