class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxx = 0

        for i in nums:
            count[i] += 1
            if maxx < count[i]:
                res = i
                maxx = count[i]
        return res

