class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        
        rows,cols = len(grid),len(grid[0])
        for r in range (rows):
            for c in range (cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    
        def bfs(r,c):
            
            if 0<=r<rows and 0<= c<cols and grid[r][c] == 1:
                
                q.append((r,c))
                grid[r][c] = 2
            return

        time = 0
        while q:
            
            for i in range(len(q)):
                r,c = q.popleft()
                bfs(r,c+1)
                bfs(r,c-1)
                bfs(r+1,c)
                bfs(r-1,c)
            if q:
                time += 1
        for r in range (rows):
            for c in range (cols):
                if grid[r][c] == 1:
                    return -1
        return time
                
              

