class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        pe = [0]*n
        po = [0]*n
        pe[0] = h[0]
        res =0

        for i in range (1,n):

            pe[i] = max(h[i],pe[i-1])
        po[n-1] = h[n-1]
        for i in range(n-2,-1,-1):
            po[i] = max(h[i], po[i+1])

        for i in range(n):
            res += min(po[i],pe[i])- h[i]

        return res