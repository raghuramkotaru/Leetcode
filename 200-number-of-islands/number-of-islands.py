class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0
        # visit = set()

        def dfs(r,c):
            grid[r][c] = "0"
            q = deque()
            q.append((r,c))
            a = [[-1,0],[1,0],[0,-1],[0,1]]
            while q:
                ro,co = q.popleft()
                
                for dr,dc in a:
                    r,c = dr+ro, dc+co
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
                        q.append((r,c))
                        grid[r][c] = "0"
                        # visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    
                    dfs(r,c)
                    count += 1
                    
        return count

        





