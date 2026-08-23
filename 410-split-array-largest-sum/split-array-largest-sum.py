class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        def check(mid):
            total =0
            count = 1
            for i in range(len(nums)):
                total += nums[i]
                if total >mid:
                    total = nums[i]
                    count += 1
            return count <= k
                


        res = r
        while l<=r:
            mid = (l+r)//2
            if check(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1

        return res

