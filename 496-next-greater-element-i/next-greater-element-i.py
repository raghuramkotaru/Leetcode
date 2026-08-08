class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        n = len(nums2)
        for i in nums1:
            ind = nums2.index(i)
            tri = 0 
            for j in range(ind+1,n):
                if nums2[j] > i:
                    ans.append(nums2[j])
                    tri =1
                    break
            if tri == 0:
                ans.append(-1)
        return ans