from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        box = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    boxid = i//3*3+j//3
                    num = board[i][j]
                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    box[boxid][num] = box[boxid].get(num, 0) + 1
                    if rows[i][num] > 1 or cols[j][num] > 1 or box[boxid][num] > 1:
                        return False
        return True