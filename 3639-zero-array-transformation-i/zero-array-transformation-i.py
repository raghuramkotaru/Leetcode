class Solution:
    def isZeroArray(self, nums, queries):
        n = len(nums)
        freq = [0] * n
        
        for q in queries:
            freq[q[0]] += 1
            if q[1] + 1 < n:
                freq[q[1] + 1] -= 1
        
        curFreq = 0
        for i in range(n):
            curFreq += freq[i]
            if curFreq < nums[i]:
                return False
        
        return True