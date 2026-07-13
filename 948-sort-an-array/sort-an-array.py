import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def rec(nums):
            if len(nums) == 1:
                return nums
            mid = len(nums)//2
            x,y= rec(nums[:mid]),rec(nums[mid:])
            return merge(x,y)

        def merge(x,y):
            res=[]
            A = len(x)
            B = len(y)
            i,j = 0, 0
            while i<A and j<B:
                if x[i] <= y[j]:
                    res.append(x[i])
                    i+=1
                else:
                    res.append(y[j])
                    j+= 1
            if i<A:
                res += x[i:]
            if j<B:
                res += y[j:]
            return res
        return rec(nums)
            

        
