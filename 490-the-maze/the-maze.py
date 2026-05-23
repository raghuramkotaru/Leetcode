class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        y, x = start
        j, i = destination
        
        dirs = [
            [0, 1], [0, -1],
            [1, 0], [-1, 0]
        ]
        
        visited = set()
        
        def in_bounds(mat, y, x):
            return (0 <= y < len(mat) and 
                    0 <= x < len(mat[0]) and 
                    mat[y][x] == 0)
        
        def dfs(y, x):
            key = (y, x)
            
            if key in visited:
                return False
            
            visited.add(key)
            
            if y == j and x == i:
                return True
            
            for dy, dx in dirs:
                y2, x2 = y, x
                
                while in_bounds(maze, y2 + dy, x2 + dx):
                    y2 += dy
                    x2 += dx
                
                if dfs(y2, x2):
                    return True
            
            return False
        
        return dfs(y, x)