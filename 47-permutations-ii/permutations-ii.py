class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        count = Counter(nums)
        cur,res = [], []
        def bk(i):
            if i == len(nums):
                res.append(cur.copy())
                return
            for n in count:
                if count[n] > 0:
                    count[n] -= 1
                    cur.append(n)
                    bk(i+1)
                    cur.pop()
                    count[n] += 1
        bk(0)
        return res


        # nums.sort()
        # cur, res = [], []
        # ind = []

        # def bk(i):
        #     if i == len(nums):
        #         res.append(cur.copy())
        #         return
        #     for j in range(len(nums)):
                
        #         if j in ind or (j > 0 and nums[j] == nums[j-1] and j-1 not in ind):
                    
        #            continue
        #         cur.append(nums[j])
        #         ind.append(j)
        #         bk(i+1)
        #         cur.pop()
        #         ind.remove(j)

        # bk(0)
        # return res
