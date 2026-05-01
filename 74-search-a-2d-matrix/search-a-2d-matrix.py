class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m = len(mat[0])
        n = len(mat)
        for i in range(n):
            
            if mat[i][m-1] >= target:
                return (self.bin(mat[i], target))
        return False
            

    def bin(self,nums, target):
        l1 = len(nums)
        l, r = 0, l1-1

        mid = (l+r)//2

        while l <= r:
            if nums[mid] == target:
                return True
                
            elif nums[mid] > target:
                r = mid -1
                mid = (l+r)//2
            else:
                l = mid+1
                mid = (l+r)//2
        return False

