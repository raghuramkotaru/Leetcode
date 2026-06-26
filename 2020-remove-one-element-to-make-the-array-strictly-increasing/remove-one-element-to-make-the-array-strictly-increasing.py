# class Solution:
#     def canBeIncreasing(self, nums: List[int]) -> bool:
#         count = 0
#         for i in range (1,len(nums)):
#             if i-2 >=0 and nums[i] < nums[i-1] and nums[i-2]< nums[i]:
#                 if count < 1:

#                     count +=1
#                 else:
#                     return False
#         return True

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        count = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                count += 1

                if count > 1:
                    return False

                # Remove nums[i-1]
                if i == 1 or nums[i] > nums[i - 2]:
                    continue

                # Remove nums[i]
                nums[i] = nums[i - 1]

        return True
        