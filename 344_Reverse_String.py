class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s)<= 1:
            return s
        i=0
        while i<= len(s)//2:
            s[i] ,s[len(s)-i-1] =s[len(s)-i-1] ,s[i]
            i+=1
        return s
        