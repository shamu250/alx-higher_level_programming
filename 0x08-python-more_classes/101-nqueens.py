#!/usr/bin/python3

import sys

def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, row, n):
    if row == n:
        # All queens are placed, print the solution
        print_solution(board, n)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, n)
            board[row][col] = 0  # Backtrack

def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

def nqueens_solver(n):
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens_util(board, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens_solver(sys.argv[1])
