#!/usr/bin/python3
"""N queens solution finder module."""

import sys


def get_input():
    """Retrieves and validates the program's argument.

    Returns:
        int: The size of the chessboard (N).
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
    return n


def is_safe(queens, row, col):
    """Checks if a queen can be placed at (row, col).

    Args:
        queens (list of int): Column positions of already placed queens.
        row (int): The row to place the queen.
        col (int): The column to place the queen.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row, queens, solutions):
    """Solves the N Queens problem using backtracking.

    Args:
        n (int): The size of the chessboard.
        row (int): The current row being considered.
        queens (list of int): Column positions of placed queens.
        solutions (list of list of list of int): All found solutions.
    """
    if row == n:
        solutions.append([[i, queens[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append(col)
            solve_nqueens(n, row + 1, queens, solutions)
            queens.pop()


def main():
    """Main function to execute the N Queens solver."""
    n = get_input()
    solutions = []
    solve_nqueens(n, 0, [], solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
