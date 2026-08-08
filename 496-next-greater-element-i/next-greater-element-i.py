class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = {n:i for i,n in enumerate(nums1)}
        res = [-1]*len(nums1)

        stack = []
        for i in nums2:

            while stack and stack[-1]<i:
                val = stack.pop()
                ind = hm[val]
                res[ind]= i
            if i in hm:
                stack.append(i)
        return res
        