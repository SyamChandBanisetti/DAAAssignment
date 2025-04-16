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
    st.header("🧭 Pathfinding Maze (DFS)")
    grid = np.zeros((10, 10), dtype=int)
    grid[3][1:9] = 1  # Add wall

    start = (0, 0)
    end = (9, 9)

    path = dfs(grid, start, end)

    fig, ax = plt.subplots()
    for i in range(10):
        for j in range(10):
            if (i, j) in path:
                color = 'green'
            elif grid[i][j] == 1:
                color = 'black'
            else:
                color = 'white'
            rect = plt.Rectangle([j, 9 - i], 1, 1, facecolor=color, edgecolor='gray')
            ax.add_patch(rect)

    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.axis('off')
    st.pyplot(fig)
