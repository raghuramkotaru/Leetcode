class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left = [float('inf')]*n
        right = [float('inf')]*n
        last = float('-inf')

        for i in range(n):
            if seats[i] == 1:
                last = i
            left[i] = i-last
        last = float('inf')
        for j in range(n-1,-1,-1):
            if seats[j] == 1:
                last = j 
            right[j] = last - j
        ans = -1
        best = -1
        for i in range(n):
            if seats[i] == 0:
                d = min(left[i],right[i])
                if d > best:
                    best = d
                    ans = i
        return best
        