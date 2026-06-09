class Solution:
    def makesquare(self, m: List[int]) -> bool:
        m.sort(reverse = True)
        l = sum(m)//4
        if sum(m) %4 != 0:
            return False
        # if max(m) > l:
        #     return False
        side = [0] * 4
        def bk(i):
            if i == len(m):
                return True

            for j in range(4):
                if side[j]+ m[i] <= l:
                    side[j] += m[i]
                    if bk(i+1):
                        return True
                    side[j] -= m[i]
            return False
        return bk(0)
        

        

