class Solution:
    def isValidSudoku(self, b : List[List[str]]) -> bool:
        col = collections.defaultdict(list)
        row = collections.defaultdict(list)
        square = collections.defaultdict(list)

        for r in range(9):
            for c in range(9):
                if b[r][c] == '.':
                    continue
                if b[r][c] in row[r] or b[r][c] in col[c]or b[r][c] in square[(r//3,c//3)]:
                    return False
                row[r].append(b[r][c])
                col[c].append(b[r][c])
                square[(r//3,c//3)].append(b[r][c])
        return True

            