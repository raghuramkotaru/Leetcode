class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1> l2:
            return False

        freq = [0]*26
        for c in s1:
            freq[ord(c)-ord('a')] +=1

        win = [0]*26
        for i in range(l1):
            win[ord(s2[i])-ord('a')] +=1
        if freq == win:
            return True
        for i in range(l1,l2):
            win[ord(s2[i])-ord('a')] +=1

            win[ord(s2[i-l1])-ord('a')] -= 1
            if freq== win:
                return True
        return False




