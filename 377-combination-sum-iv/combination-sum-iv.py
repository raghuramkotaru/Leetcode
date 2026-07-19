class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        count = 0
        memo = {}
        def dfs(n):
            nonlocal count
            if n in memo:
                return memo[n]
            
            if n == target:
                return 1
            if n > target:
                return 0
            ans = 0
            for i in nums:
                
                ans += dfs(n+i)
            memo[n] = ans
            return ans
            
        return dfs(0)
            



























        # dp = [0] * (target + 1)
        # dp[0] = 1
        
        # for i in range(1, target + 1):
        #     for num in nums:
        #         if i - num >= 0:
        #             dp[i] += dp[i - num]
                    
        # return dp[target]