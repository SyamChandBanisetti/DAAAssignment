import streamlit as st
from collections import deque
import numpy as np

goal_state = [[1,2,3],[4,5,6],[7,8,0]]

def get_neighbors(state):
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    moves = []
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)
    return moves

def bfs(start):
    visited = set()
    queue = deque([(start, [])])
    while queue:
        current, path = queue.popleft()
        state_tuple = tuple(map(tuple, current))
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        if current == goal_state:
            return path + [current]
        for neighbor in get_neighbors(current):
            queue.append((neighbor, path + [current]))
    return []

def run_puzzle8_app():
    st.header("🧩 8-Puzzle Solver (BFS)")
    start_state_input = st.text_input("Enter initial state (comma-separated, 0 as blank):", "1,2,3,4,0,6,7,5,8")
    if st.button("Solve"):
        try:
            flat = list(map(int, start_state_input.strip().split(",")))
            assert len(flat) == 9
            start_state = [flat[i*3:(i+1)*3] for i in range(3)]
            solution_path = bfs(start_state)
            if solution_path:
                st.success(f"Solved in {len(solution_path)-1} moves!")
                for idx, board in enumerate(solution_path):
                    st.markdown(f"**Step {idx}**")
                    st.table(board)
            else:
                st.error("No solution found.")
        except:
            st.error("Invalid input. Enter 9 numbers separated by commas.")
