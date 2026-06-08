class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        p = []

        def bk(start,i):
            if i == k:
                res.append(p.copy())
                return
            for j in range(start,n+1):
                p.append(j)
                bk(j+1,i+1)
                p.pop()
        bk(1,0)
        return res

