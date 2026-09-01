class Solution:
    def minimumSteps(self, s: str) -> int:
        count, black = 0,0
        for i in s:
            if i == '1':
                black+=1
            else:
                count += black
        return count