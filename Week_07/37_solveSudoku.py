from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def backtrace(idx):
            if idx == len(tofilled):
                return True
            row, col = tofilled[idx]
            boxid = row//3*3+ col//3
            for num in rows[row] & cols[col] & box[boxid]:
                rows[row].remove(num)
                cols[col].remove(num)
                box[boxid].remove(num)
                board[row][col] = str(num)
                if backtrace(idx+1):
                    return True
                rows[row].add(num)
                cols[col].add(num)
                box[boxid].add(num)
            return False


        rows = [set(range(1,10)) for _ in range(9)]
        cols = [set(range(1, 10)) for _ in range(9)]
        box = [set(range(1, 10)) for _ in range(9)]
        tofilled = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    n = int(board[i][j])
                    rows[i].remove(n)
                    cols[j].remove(n)
                    box[i//3*3 + j//3].remove(n)
                else:
                    tofilled.append((i,j))
        backtrace(0)