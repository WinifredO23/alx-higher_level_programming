#!/usr/bin/python3
"""Solves the N-queens puzzle.
"""

import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at the given row and column."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def print_solution(board):
    """Print the current solution in the required format."""
    n = len(board)
    solution = [[i, col] for i, col in enumerate(board)]
    print(solution)


def solve_n_queens(n):
    """Initialize the chessboard and find all solutions."""
    board = [-1] * n
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions


def solve_n_queens_util(board, row, n, solutions):
    """Recursive function to find all solutions."""
    if row == n:
        solutions.append(list(board))
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens_util(board, row + 1, n, solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        """Check for the correct number of arguments"""
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        """Check if N is a valid integer"""
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        """Check if N is at least 4"""
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(n)
    for solution in solutions:
        print_solution(solution)
