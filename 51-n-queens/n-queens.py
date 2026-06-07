class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for rows in range(n)]
        col = set()
        nd = set()
        pd = set()
        def bk(r):
            if r == n:
                copy = ["".join(rows) for rows in board]
                res.append(copy)
                return
            for c in range (n):
                if c in col or (r+c) in pd or (r-c) in nd:
                    continue 
                col.add(c)
                pd.add(r+c)
                nd.add(r-c)
                board[r][c] = "Q"
                bk(r+1)

                col.remove(c)
                pd.remove(r+c)
                nd.remove(r-c)
                board[r][c] = "."
        bk(0)
        return res
