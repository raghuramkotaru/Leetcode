class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ma = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                ma = max(ma,count)
                count = 0
        return max(ma,count)