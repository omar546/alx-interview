#!/usr/bin/python3
"""
Solution to the N-Queens problem.
"""
import sys
from typing import List, Set

def backTracker(row: int, n: int, cols: Set[int], pos_diag: Set[int], neg_diag: Set[int], board: List[List[int]]) -> None:
    """
    Backtracking function to find all solutions.
    Args:
        row (int): Current row to place a queen.
        n (int): Size of the board (n x n).
        cols (Set[int]): Set of columns where queens are already placed.
        pos_diag (Set[int]): Set of positive diagonals where queens are already placed.
        neg_diag (Set[int]): Set of negative diagonals where queens are already placed.
        board (List[List[int]]): Current state of the board.
    """
    if row == n:
        solution = [[r, c] for r in range(n) for c in range(n) if board[r][c] == 1]
        print(solution)
        return

    for col in range(n):
        pos_diagonal = row + col
        neg_diagonal = row - col
        
        if col in cols or pos_diagonal in pos_diag or neg_diagonal in neg_diag:
            continue

        cols.add(col)
        pos_diag.add(pos_diagonal)
        neg_diag.add(neg_diagonal)
        board[row][col] = 1

        backTracker(row + 1, n, cols, pos_diag, neg_diag, board)

        # Backtrack
        cols.remove(col)
        pos_diag.remove(pos_diagonal)
        neg_diag.remove(neg_diagonal)
        board[row][col] = 0

def nqueenSolver(n: int) -> None:
    """
    Solves the N-Queens problem.
    Args:
        n (int): Number of queens. Must be >= 4.
    """
    cols: Set[int] = set()
    pos_diag: Set[int] = set()
    neg_diag: Set[int] = set()
    board: List[List[int]] = [[0] * n for _ in range(n)]

    backTracker(0, n, cols, pos_diag, neg_diag, board)

def main() -> None:
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
