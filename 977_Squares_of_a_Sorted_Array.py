class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k =[]
        for i in nums1:
            if i in nums2:
                k.append(i)
        return list(set(k))        