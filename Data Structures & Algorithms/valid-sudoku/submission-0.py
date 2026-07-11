class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)
        m = len(board[0])

        # for row
        for i in range(n):
            seen = set()
            for j in range(m):
                cell = board[i][j]

                if cell == '.':
                    continue
                if cell in seen:
                    return False
                seen.add(cell)

        # for column
        for i in range(n):
            seen = set()
            for j in range(m):
                cell = board[j][i]
                
                if cell == '.':
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
        
        # 3 x 3 boxes
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                seen = set()
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        cell = board[r][c]
                
                        if cell == '.':
                            continue
                        if cell in seen:
                            return False
                        seen.add(cell)

        return True
