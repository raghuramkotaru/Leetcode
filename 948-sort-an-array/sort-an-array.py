import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # bucket sort
        minn = min(nums)
        maxx =  max(nums)
        bucket = [0]*(maxx-minn+1)

        for n in nums:
            bucket[n-minn] +=1
        res = []
        for i,count in enumerate(bucket):
            while count>0:
                res.append(i+minn)
                count -= 1
        return res









        # def rec(nums):
        #     if len(nums) == 1:
        #         return nums
        #     mid = len(nums)//2
        #     x,y= rec(nums[:mid]),rec(nums[mid:])
        #     return merge(x,y)

        # def merge(x,y):
        #     res=[]
        #     A = len(x)
        #     B = len(y)
        #     i,j = 0, 0
        #     while i<A and j<B:
        #         if x[i] <= y[j]:
        #             res.append(x[i])
        #             i+=1
        #         else:
        #             res.append(y[j])
        #             j+= 1
        #     if i<A:
        #         res += x[i:]
        #     if j<B:
        #         res += y[j:]
        #     return res
        # return rec(nums)
            

        
