class Solution:
    
    def minOperations(self, nums: list[int]) -> int:
        return sum(max(0, nums[i] - nums[i + 1]) for i in range(len(nums) - 1))