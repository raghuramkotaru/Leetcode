class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        i = 0 
        j = n-1

        while j< len(s2):
            x= "".join(sorted(s2[i:j+1]))
            y= "".join(sorted(s1))
            if x==y:
                return True
            i += 1
            j += 1
        return False
