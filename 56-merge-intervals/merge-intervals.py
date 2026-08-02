class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda i:i[0])
        merged = [intervals[0]]
        for i in range(1,len(intervals)):
            left = merged[-1][1]
            right = intervals[i][0]
            if left >= right:
                curr_mur = [merged[-1][0],max(left,intervals[i][1])]
                merged[-1] = curr_mur
                continue
            merged.append(intervals[i])
        return merged
            

            


            