class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows,cols = len(grid),len(grid[0])
        count = 0
        ma = 0
        for r in range (rows):
            for c in range (cols):
                count = 0
                if grid[r][c] == 0:
                    continue
                count+=1
                n = []
                n.append((r,c))
                grid[r][c] = 0
                while n:
                    ro,co = n.pop()
                    if ro+1 < rows and grid[ro+1][co] == 1:
                        count+= 1
                        n.append((ro+1,co))
                        grid[ro+1][co] = 0
                    if ro-1 >= 0 and grid[ro-1][co] == 1:
                        count+= 1
                        n.append((ro-1,co))
                        grid[ro-1][co] = 0
                    if co+1 < cols and grid[ro][co+1] == 1:
                        count+= 1
                        n.append((ro,co+1))
                        grid[ro][co+1] = 0
                    if co-1 >= 0 and grid[ro][co-1] == 1:
                        count+= 1
                        n.append((ro,co-1))
                        grid[ro][co-1] = 0
                ma= max(ma,count)
        return ma
                    
        