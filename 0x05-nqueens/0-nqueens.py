#!/usr/bin/python3
"""
module: ..
the strongest female chess player of all time
return: ..
"""
from sys import argv, exit


def solveNQueens(n):
    """Solving the N queens problem"""
    res = []
    queens = [-1] * n

    def dfs(index):
        """Resolving the N queens problem"""
        if index == len(queens):
            res.append(queens[:])
            return
        for i in range(len(queens)):
            queens[index] = i
            if valid(index):
                dfs(index + 1)

    # check whether nth queens can be placed.
    def valid(n):
        """Method that checks the valid of position in board"""
        for i in range(n):
            if abs(queens[i] - queens[n]) == n - i or queens[i] == queens[n]:
                return False
        return True

    def make_all_boards(res):
        """Method that builts List to be returned"""
        actual_boards = []
        for queens in res:
            board = []
            for row, col in enumerate(queens):
                board.append([row, col])
            actual_boards.append(board)
        return actual_boards

    dfs(0)
    return make_all_boards(res)

if __name__ == "__main__":
    if len(argv) < 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)
    else:
        result = solveNQueens(n)
        for row in result:
            print(row)
