import streamlit as st
import pandas as pd

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True

def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []

    def backtrack(col):
        if col == n:
            solutions.append([row[:] for row in board])
            return
        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                backtrack(col + 1)
                board[row][col] = 0

    backtrack(0)
    return solutions

def run_nqueens_app():
    st.header("👑 N-Queens Solver")
    n = st.slider("Select board size (N)", min_value=4, max_value=12, value=8)
    if st.button("Solve"):
        solutions = solve_nqueens(n)
        st.success(f"Found {len(solutions)} solutions! Showing first 3 below.")
        for idx, sol in enumerate(solutions[:3]):
            st.markdown(f"**Solution {idx+1}**")
            st.dataframe(pd.DataFrame(sol))
