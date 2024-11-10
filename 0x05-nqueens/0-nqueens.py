#!/usr/bin/python3
import sys

def ChessBoard(n: int):
    """Solving N queens problem with Backtracking algorithm.
    Args:
        n (int): non-attacking queens to place on board.

    Returns:
        List[List[int]]: list of columns & rows of where queens are placed.
    """
    result = []

    def checkBoard(row, col, col_in_row):
        """Checks if a queen can be placed without attacking other queens."""
        for r in range(row):
            if col_in_row[r] == col or row - r == abs(col - col_in_row[r]):
                return False
        return True

    def saveBoard(col_in_row):
        """Saves the current state of the board as a solution."""
        solution = [[i, col_in_row[i]] for i in range(n)]
        result.append(solution)

    def placeQueen(row, cols, col_in_row):
        """Places non-attacking queens on an n x n chessboard."""
        if row == n:
            saveBoard(col_in_row)
            return
        for col in range(n):
            if cols[col] == 0 and checkBoard(row, col, col_in_row):
                cols[col] = 1
                col_in_row[row] = col
                placeQueen(row + 1, cols, col_in_row)
                cols[col] = 0

    placeQueen(0, [0] * n, [0] * n)
    return result

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens = ChessBoard(int(sys.argv[1]))
    for queens in nqueens:
        print(queens)
