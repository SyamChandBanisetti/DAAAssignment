import streamlit as st

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] or \
           (row - i >= 0 and board[row - i][col - i]) or \
           (row + i < n and board[row + i][col - i]):
            return False
    return True

def solve_nqueens(n):
    board = [[0]*n for _ in range(n)]
    solutions = []

    def backtrack(col):
        if col == n:
            solutions.append([row[:] for row in board])
            return
        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                backtrack(col+1)
                board[row][col] = 0

    backtrack(0)
    return solutions

def run_nqueens_app():
    st.header("👑 N-Queens Solver")
    n = st.slider("Select size of board (N)", 4, 12, 8)
    if st.button("Solve"):
        solutions = solve_nqueens(n)
        st.success(f"Found {len(solutions)} solutions!")
        for idx, sol in enumerate(solutions[:3]):
            st.text(f"Solution {idx+1}")
            st.table(sol)
