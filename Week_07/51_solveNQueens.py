from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def could_place(row, col):
            return not(cols[col] + hill_diagonals[row+col] + dale_diagonals[row-col])

        def place_queue(row, col):
            queue.add((row, col))
            cols[col] = 1
            hill_diagonals[row + col] = 1
            dale_diagonals[row - col] = 1

        def add_solution():
            solution = []
            for row, col in sorted(queue):
                solution.append('.'* col + 'Q' + '.'*(n-col-1))
            output.append(solution)

        def remove_queue(row,col):
            queue.remove((row, col))
            cols[col] = 0
            hill_diagonals[row + col] = 0
            dale_diagonals[row - col] = 0

        def backtrace(row):
            for col in range(n):
                if could_place(row, col):
                    place_queue(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrace(row + 1)
                    remove_queue(row, col)

        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)
        queue = set()
        output = []
        backtrace(0)
        return output