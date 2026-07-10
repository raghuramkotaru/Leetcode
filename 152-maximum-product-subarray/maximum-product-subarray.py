class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        ma,mi =1,1
        for n in nums:
            if n==0:
                ma,mi=1,1
                continue
            temp = ma
            ma = max(n*ma, n*mi, n)
            mi = min(temp*n, mi*n, n)
            res = max(ma,mi,res)
        return res