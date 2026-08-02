class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l,h,curr= 0 , len(nums)-1, 0 
        while curr <= h:
            if nums[curr] == 0:
                nums[curr], nums[l] = nums[l],nums[curr]
                curr+=1
                l+=1
            elif nums[curr] ==1:
                curr += 1
            else:
                nums[curr], nums[h] = nums[h],nums[curr]
                h -= 1
                
        
        return nums


        