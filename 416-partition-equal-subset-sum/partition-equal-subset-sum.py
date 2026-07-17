class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 !=0:
            return False
        target = total//2
        
        dp = set()
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            newdp = set()
            for j in dp:
                newdp.add(nums[i]+j)
                newdp.add(j)
            dp = newdp
        return True if target in dp else False
