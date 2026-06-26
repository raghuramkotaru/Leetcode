# class Solution:
#     def canBeIncreasing(self, nums: List[int]) -> bool:
#         count = 0
#         for i in range (1,len(nums)):
#             if nums[i] <= nums[i-1]:
#                 count +=1
#                 if count>1:
#                     return False
#                 if i==1 or nums[i]>nums[i-2]:
#                     continue
#                 nums[i] = nums[i-1]
#         return True
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def is_increasing(arr):
            # Helper to check if array is strictly increasing
            for i in range(1, len(arr)):
                if arr[i] <= arr[i-1]:
                    return False
            return True
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                # Test both removal scenarios: skip nums[i-1] or skip nums[i]
                without_prev = nums[:i-1] + nums[i:]  # Remove nums[i-1]
                without_curr = nums[:i] + nums[i+1:]  # Remove nums[i]
                return is_increasing(without_prev) or is_increasing(without_curr)
        return True  # Already strictly increasing