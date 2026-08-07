class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        if n == 1: return nums
        k = k%n
        l1 = nums[n-k:]
        l2 = nums[:n-k]
        nums[:] = l1+l2