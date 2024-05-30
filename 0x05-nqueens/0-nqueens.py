#!/usr/bin/python3
"""
Solution to the N-Queens problem.
"""
import sys

def backTracker(row, n, cols, pos_diag, neg_diag, board):
    """
    Backtracking function to find all solutions.
    Args:
        row (int): Current row to place a queen.
        n (int): Size of the board (n x n).
        cols (set): Set of columns where queens are already placed.
        pos_diag (set): Set of positive diagonals where queens are already placed.
        neg_diag (set): Set of negative diagonals where queens are already placed.
        board (list): Current state of the board.
    """
    if row == n:
        solution = [[r, c] for r in range(n) for c in range(n) if board[r][c] == 1]
        print(solution)
        return

    for col in range(n):
        if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
            continue

        cols.add(col)
        pos_diag.add(row + col)
        neg_diag.add(row - col)
        board[row][col] = 1

        backTracker(row + 1, n, cols, pos_diag, neg_diag, board)

        cols.remove(col)
        pos_diag.remove(row + col)
        neg_diag.remove(row - col)
        board[row][col] = 0

def nqueenSolver(n):
    """
    Solves the N-Queens problem.
    Args:
        n (int): Number of queens. Must be >= 4.
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for _ in range(n)]

    backTracker(0, n, cols, pos_diag, neg_diag, board)

def main():
    """
    Main function to parse command-line arguments and initiate the solver.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueenSolver(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

if __name__ == "__main__":
    main()
