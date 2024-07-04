#!/usr/bin/python3
"""nqueen"""

import sys


def generate_solutions(n):
    """solution
    """
    solutions = [[]]
    for queen in range(n):
        solutions = place_queen(queen, n, solutions)
    return solutions


def place_queen(queen, n, prev_solutions):
    """queen placement
    """
    safe_positions = []
    for solution in prev_solutions:
        for column in range(n):
            if is_safe(queen, column, solution):
                safe_positions.append(solution + [column])
    return safe_positions


def is_safe(queen, column, solution):
    """safety
    """
    for q, c in enumerate(solution):
        if c == column or abs(c - column) == abs(q - queen):
            return False
    return True


def init():
    """initialize
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def n_queens():
    n = init()
    solutions = generate_solutions(n)
    for solution in solutions:
        formatted_solution = [
            [row, column] for row, column in enumerate(solution)]
        print(formatted_solution)


if __name__ == '__main__':
    n_queens()
