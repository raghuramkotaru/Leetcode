class Solution:
    def twoSum(self, n: List[int], k: int) -> List[int]:
        i,j = 0, len(n)-1
        while i<j:
            if n[i]+n[j] == k:
                return([i+1,j+1])
            if n[i]+n[j] > k:
                j-=1
            if n[i]+n[j]<k:
                i += 1
        
            
            # if i+j<k:


