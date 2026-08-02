class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list(s).sort()
        list(t).sort()
        return s==t