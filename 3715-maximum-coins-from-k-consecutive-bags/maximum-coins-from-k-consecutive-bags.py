class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        n = len(coins)
        def solve(A):
            A.sort()
            ans = window = j = 0

            for i ,(l,r,c) in enumerate(A):
                while j+1<n and A[j+1][0]< l+k:
                    lj,rj,cj =  A[j]
                    window += (rj-lj+1)*cj
                    j += 1
                extra = 0
                if j <n and A[j][0]<l+k:
                    rightmost = min(l+k-1,A[j][1])
                    length = rightmost-A[j][0]+1
                    extra = length*A[j][2]
                ans = max(ans,window+extra)
                
                window -= (r-l+1)*c
            return ans
        ans = solve(coins)
        for i ,(l,r,c) in enumerate(coins):
            coins[i] = [-r,-l,c]
        ans = max(ans,solve(coins))
        return ans