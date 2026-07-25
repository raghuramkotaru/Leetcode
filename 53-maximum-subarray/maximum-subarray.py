class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum = 0
        maxx = nums[0]

        for i in range(len(nums)):
            if running_sum < 0:
                running_sum = 0
            running_sum += nums[i]
            maxx = max(maxx, running_sum)
        return maxx