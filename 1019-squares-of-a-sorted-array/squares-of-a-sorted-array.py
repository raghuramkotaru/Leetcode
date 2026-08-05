class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = n-1
        res = [0]*n
        for x in range(n-1,-1,-1):
            if abs(nums[i]) > abs(nums[j]):
                res[x] = nums[i]*nums[i]
                i += 1
            else:
                res[x] = nums[j]*nums[j]
                j -=1
        return res