class Solution:
    def validPalindrome(self, s: str) -> bool:
        left =0
        right =len(s) -1
        flag =False
        while left < right :
            if s[left] != s[right] :
                if flag == False:
                    flag =True
                    if s[left +1]== s[right]:
                        left =left +1
                    elif s[left] ==s[right-1]:
                        right =right -1
                    continue
                return False
            left +=1
            right -=1
        return True
            


