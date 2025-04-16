import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def dfs(grid, start, end, visited=None, path=None):
    if visited is None: visited = set()
    if path is None: path = []
    if start == end:
        return path + [end]
    x, y = start
    visited.add((x, y))
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0 and (nx, ny) not in visited:
            result = dfs(grid, (nx, ny), end, visited, path + [start])
            if result:
                return result
    return []

def run_pathfinder_app():
    st.header("🧭 Pathfinding Maze (DFS Solver)")

    with st.expander("ℹ️ How to use this app (Step-by-step Guide)"):
        st.markdown("""
        This app helps you solve a **maze** using **DFS (Depth-First Search)**. Follow the steps below to build your own maze and see if there's a path from start to end.

        ---
        ### 🧩 Step-by-Step Instructions:
        
        1. **Choose Grid Size**  
           - Use the slider to pick the size of your maze (from 5x5 to 15x15).  
           - Default is 10x10.

        2. **Place Walls**  
           - Use the slider to set how many walls you'd like to place.  
           - For each wall, pick its row and column position.  
           - These walls are black blocks the algorithm cannot pass through.

        3. **Set Start and End Points**  
           - Choose the row and column where the maze starts (`🟦`) and ends (`🟥`).  
           - Make sure start/end aren’t placed on top of walls!

        4. **Click 'Solve Maze'**  
           - This triggers the DFS algorithm to try to find a path from start to end.  
           - If a path exists, you’ll see it marked in green (`🟩`).

        ---
        ### 🔍 Legend:
        - 🟦 Start
        - 🟥 End
        - ⬛ Wall
        - 🟩 Path (if found)
        - ⬜ Open space

        ---
        Feel free to experiment by changing walls, grid size, or start/end positions!
        """)

    grid_size = st.slider("🔲 Grid size", 5, 15, 10)
    grid = np.zeros((grid_size, grid_size), dtype=int)

    st.subheader("🚧 Set Walls")
    num_walls = st.slider("Number of walls", 0, grid_size * 2, 10)

    wall_positions = []
    for i in range(num_walls):
        col1, col2 = st.columns(2)
        with col1:
            wx = st.number_input(f"Wall {i+1} Row", min_value=0, max_value=grid_size-1, key=f"wx_{i}")
        with col2:
            wy = st.number_input(f"Wall {i+1} Col", min_value=0, max_value=grid_size-1, key=f"wy_{i}")
        wall_positions.append((int(wx), int(wy)))
        grid[int(wx)][int(wy)] = 1

    st.subheader("🏁 Set Start and End Points")
    col1, col2 = st.columns(2)
    with col1:
        start_x = st.number_input("Start Row", 0, grid_size-1, 0)
        start_y = st.number_input("Start Col", 0, grid_size-1, 0)
    with col2:
        end_x = st.number_input("End Row", 0, grid_size-1, grid_size-1)
        end_y = st.number_input("End Col", 0, grid_size-1, grid_size-1)

    start = (int(start_x), int(start_y))
    end = (int(end_x), int(end_y))

    if grid[start] == 1 or grid[end] == 1:
        st.warning("Start or End point cannot be on a wall.")
        return

    if st.button("🧭 Solve Maze"):
        path = dfs(grid, start, end)

        fig, ax = plt.subplots()
        for i in range(grid_size):
            for j in range(grid_size):
                if (i, j) in path:
                    color = 'green'
                elif (i, j) == start:
                    color = 'blue'
                elif (i, j) == end:
                    color = 'red'
                elif grid[i][j] == 1:
                    color = 'black'
                else:
                    color = 'white'
                rect = plt.Rectangle([j, grid_size - 1 - i], 1, 1, facecolor=color, edgecolor='gray')
                ax.add_patch(rect)

        plt.xlim(0, grid_size)
        plt.ylim(0, grid_size)
        plt.axis('off')
        st.pyplot(fig)

        if path:
            st.success(f"✅ Path found! Steps: {len(path) - 1}")
        else:
            st.error("🚫 No path found.")
