class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s2=list(s)
        t2=list(t)
        s2.sort()
        t2.sort()
        return s2==t2