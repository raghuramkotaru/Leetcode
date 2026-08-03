class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ma = 0
        count = 0
        for i in range(len(nums)):
            if nums[i]== 1:
                count+=1
            if nums[i]==0 or i+1 == len(nums):
                ma = max(ma,count)
                count = 0

        return ma

