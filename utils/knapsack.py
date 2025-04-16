# knapsack_solver.py
import streamlit as st

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(n):
        for w in range(capacity + 1):
            if weights[i] <= w:
                dp[i + 1][w] = max(dp[i][w], dp[i][w - weights[i]] + values[i])
            else:
                dp[i + 1][w] = dp[i][w]
    return dp[n][capacity]

def run_knapsack_app():
    st.header("🎒 Knapsack Solver (0/1)")
    st.markdown("This uses **Dynamic Programming** to maximize the value within a given weight capacity.")

    weights_input = st.text_input("Enter item weights (comma-separated):", "2,3,4,5")
    values_input = st.text_input("Enter item values (comma-separated):", "3,4,5,6")
    capacity = st.slider("Select knapsack capacity", 1, 50, 10)

    weights = list(map(int, weights_input.strip().split(",")))
    values = list(map(int, values_input.strip().split(",")))

    if st.button("💼 Solve"):
        max_value = knapsack(weights, values, capacity)
        st.success(f"✅ Maximum value that can be carried: {max_value}")
