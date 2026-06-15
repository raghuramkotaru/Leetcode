class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visit =set()
        fresh = 0
        rows,cols = len(grid),len(grid[0])
        for r in range (rows):
            for c in range (cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
                if grid[r][c]== 1:
                    fresh+= 1
        def bfs(r,c):
            nonlocal fresh
            if 0<=r<rows and 0<= c<cols and grid[r][c] == 1 and (r,c) not in visit:
                visit.add((r,c))
                q.append((r,c))
                grid[r][c] = 2
                fresh -= 1
            return

        time = 0
        while q and fresh > 0:
            
            for i in range(len(q)):
                r,c = q.popleft()
                bfs(r,c+1)
                bfs(r,c-1)
                bfs(r+1,c)
                bfs(r-1,c)
            time += 1
        
        return time if fresh == 0 else -1
                
              



