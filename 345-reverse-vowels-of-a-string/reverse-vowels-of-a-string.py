class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vov = set('aeiouAEIOU')

        l = 0
        r = len(s)-1
        while l<r:
            while l<r and s[l]not in vov:
                l += 1
            while l<r and s[r]not in vov:
                r -= 1
            s[l],s[r] = s[r],s[l]
            l +=1
            r -= 1
        s = "".join(s)
        return s