class Solution:

    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        subset = []
        def dfs(i):
            res.append(subset.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                subset.append(nums[j])
                dfs(j + 1)
                subset.pop()
        dfs(0)
        return res
# class Solution:
#     def subsetsWithDup(self, nums):
#         res = []
#         subset = []
#         nums.sort()
#         def dfs(i):
        
#             if i == len(nums):
#                 if subset not in res:
#                     res.append(subset.copy())
#                 return
#             subset.append(nums[i])
#             dfs(i+1)
#             subset.pop()
#             dfs(i+1)
#         dfs(0)

#         return res
