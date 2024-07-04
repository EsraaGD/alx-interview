#!/usr/bin/python3
"""
This script solves the N-Queens problem for a given board size N.
It finds all possible arrangements of N queens on an N×N chessboard
such that no two queens threaten each other.
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].

    Args:
        board (list of list of int): The current state of the board.
        row (int): The row index to check.
        col (int): The column index to check.

    Returns:
        bool: True if no other queens attack this position, False otherwise.
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, solutions):
    """
    Utilizes backtracking to find all solutions for the N-queens problem.

    Args:
        board (list of list of int): The current state of the board.
        col (int): The current column index being processed.
        solutions : Accumulator for all valid solutions found.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if col >= len(board):
        # Convert board into the solution format
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place queen
            res = solve_nqueens_util(board, col + 1, solutions) or res
            board[i][col] = 0  # Backtrack

    return res


def solve_nqueens(n):
    """
    Solves the N-queens problem for a board of size n x n.

    Args:
        n (int): The size of the board.

    Returns:
        l of l of l of int: Each sol is represented as list of [r, c] pairs.
    """
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    return solutions


def main():
    """
    Main entry point for the N-queens problem solver.
    Handles argument parsing and validation, then prints solutions.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
