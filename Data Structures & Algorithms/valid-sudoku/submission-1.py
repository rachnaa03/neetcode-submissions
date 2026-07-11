class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)
        m = len(board[0])

        row = [set() for _ in range(n)]
        col = [set() for _ in range(n)]
        box = [set() for _ in range(n)]

        for r in range(n):
            for c in range(m):
                cell = board[r][c]
                box_idx = (r // 3) * 3 + (c // 3)

                if cell == '.':
                    continue
                if cell in row[r] or cell in col[c] or cell in box[box_idx]:
                    return False
                row[r].add(cell)
                col[c].add(cell)
                box[box_idx].add(cell)
                
        return True




