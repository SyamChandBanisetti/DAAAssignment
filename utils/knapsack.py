import streamlit as st

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(n):
        for w in range(capacity+1):
            if weights[i] <= w:
                dp[i+1][w] = max(dp[i][w], values[i] + dp[i][w - weights[i]])
            else:
                dp[i+1][w] = dp[i][w]
    return dp[-1][-1]

def run_knapsack_app():
    st.header("📦 Knapsack Optimizer")
    weights = st.text_input("Enter weights (comma-separated)", "2,3,4,5")
    values = st.text_input("Enter values (comma-separated)", "3,4,5,6")
    capacity = st.slider("Knapsack Capacity", 1, 20, 10)

    if st.button("Optimize"):
        w_list = list(map(int, weights.split(",")))
        v_list = list(map(int, values.split(",")))
        max_val = knapsack(w_list, v_list, capacity)
        st.success(f"Maximum value that can be carried: {max_val}")
