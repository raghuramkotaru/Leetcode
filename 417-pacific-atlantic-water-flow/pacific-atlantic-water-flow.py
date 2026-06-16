class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pec, atl = set(),set()
        rows,cols = len(heights), len(heights[0])
        
        def dfs(r,c,visit,h):
            if r<0 or r==rows or c < 0 or c==cols or heights[r][c] < h or (r,c) in visit:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for c in range(cols):
            dfs(0,c,pec,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        for r in range(rows):
            dfs(r,0,pec,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        res = []
        for r in range (rows):
            for c in range(cols):
                if (r,c) in pec and (r,c) in atl:
                    res.append([r,c])
        return res