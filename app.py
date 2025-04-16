import streamlit as st
from utils.nqueens import run_nqueens_app
from utils.puzzle8 import run_8puzzle_app
from utils.pathfinder import run_pathfinder_app
from utils.knapsack import run_knapsack_app

st.set_page_config(page_title="DAA Interactive Solver", layout="wide")
st.title("🧠 Design & Analysis of Algorithms Playground")

problem = st.sidebar.selectbox("Choose a Problem to Explore", [
    "8-Puzzle Solver", 
    "N-Queens Problem", 
    "Pathfinding Maze", 
    "Knapsack (Zip Optimization)"
])

if problem == "8-Puzzle Solver":
    run_puzzle8_app()
elif problem == "N-Queens Problem":
    run_nqueens_app()
elif problem == "Pathfinding Maze":
    run_pathfinder_app()
elif problem == "Knapsack (Zip Optimization)":
    run_knapsack_app()
