# 8_puzzle_solver.py
import streamlit as st
import heapq

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Heuristic function: Manhattan Distance
def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val - 1) // 3
                goal_y = (val - 1) % 3
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

# Find position of 0 (blank)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)

# Generate all valid next states
def get_neighbors(state):
    x, y = find_zero(state)
    neighbors = []
    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Check if two boards are equal
def same(state1, state2):
    return all(state1[i][j] == state2[i][j] for i in range(3) for j in range(3))

# A* Algorithm
def solve_puzzle(start):
    queue = [(manhattan(start), 0, start, [])]
    visited = set()
    while queue:
        est_total, cost, state, path = heapq.heappop(queue)
        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        if same(state, goal_state):
            return path + [state]
        for neighbor in get_neighbors(state):
            heapq.heappush(queue, (
                cost + 1 + manhattan(neighbor),
                cost + 1,
                neighbor,
                path + [state]
            ))
    return []

def run_8puzzle_app():
    st.header("🧩 8-Puzzle Solver")
    st.markdown("""
    This puzzle challenges you to rearrange tiles into the correct order using only the empty space to slide tiles around.  
    The algorithm will find the optimal steps using **A\* Search** and **Manhattan Distance** as a heuristic.
    """)

    default = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    st.markdown("### Enter your 3x3 puzzle (use 0 for the empty tile):")
    user_input = []
    for i in range(3):
        row = st.text_input(f"Row {i+1} (comma-separated)", value=",".join(map(str, default[i])))
        user_input.append(list(map(int, row.strip().split(','))))

    if st.button("🧠 Solve"):
        st.write("Solving the puzzle...")
        steps = solve_puzzle(user_input)
        if not steps:
            st.error("❌ No solution found. Try a different configuration.")
        else:
            st.success(f"✅ Puzzle Solved in {len(steps)-1} moves.")
            for idx, state in enumerate(steps):
                st.markdown(f"**Step {idx}**")
                st.table(state)
