class Solution:
    def validPalindrome(self, s: str) -> bool:
        count =0
        l = 0 
        r = len(s)-1
        def ispal(l,r):
            while l<=r:
                if s[l]!= s[r]:
                    return False
                l+= 1
                r -= 1
            return True
            
        while l<=r:
            if s[l] != s[r]:
                return ispal(l+1, r) or ispal(l, r-1)
                    
                
            r-=1
            l+=1
        return True
        
        
        