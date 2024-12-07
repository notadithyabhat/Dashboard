import streamlit as st
import pandas as pd
import gurobipy as gp
from gurobipy import GRB

# Set up the page title
st.title("Optimization: Equipment Allocation")

# Description of the work
st.markdown("""
### Optimization Problem
This page demonstrates an optimization model designed to allocate available equipment to various program types based on usage counts. The objective is to maximize the total usage of equipment while adhering to the following constraints:
- Each piece of equipment can only be allocated to one program type at a time.
- Program types must share equipment optimally to maximize overall usage.

**Goal**: Ensure optimal utilization of equipment across program types.
""")

# File upload for equipment usage data
uploaded_file = st.file_uploader("Upload Equipment Usage Data (CSV)", type="csv")

if uploaded_file:
    # Load the data
    data = pd.read_csv(uploaded_file)

    st.markdown("### Uploaded Data")
    st.write(data)

    # Extract unique program types and equipment names
    program_types = data['Program_type'].unique().tolist()
    equipment_names = data['Equipment_Name'].unique().tolist()

    # Create a dictionary of usage counts
    usage_counts = {}
    for _, row in data.iterrows():
        if row['Program_type'] not in usage_counts:
            usage_counts[row['Program_type']] = {}
        usage_counts[row['Program_type']][row['Equipment_Name']] = row['Usage_Count']

    # Optimization Model
    model = gp.Model("Equipment Allocation")
    x = model.addVars(program_types, equipment_names, vtype=GRB.BINARY, name="x")

    # Objective: Maximize total usage count
    model.setObjective(
        gp.quicksum(x[i, j] * usage_counts.get(i, {}).get(j, 0) for i in program_types for j in equipment_names),
        GRB.MAXIMIZE
    )

    # Constraints
    # Equipment availability
    for j in equipment_names:
        model.addConstr(
            gp.quicksum(x[i, j] for i in program_types) <= 1,
            name=f"Equipment_Availability_{j}"
        )

    # Optimize the model
    model.optimize()

    # Display results
    if model.status == GRB.OPTIMAL:
        st.markdown("### Optimal Equipment Allocation")
        results = []
        for i in program_types:
            for j in equipment_names:
                if x[i, j].x > 0.5:
                    results.append({"Program Type": i, "Equipment": j, "Usage Count": usage_counts[i][j]})

        results_df = pd.DataFrame(results)
        st.table(results_df)

        # Visualize the results
        st.markdown("### Allocation Summary")
        allocation_summary = results_df.groupby("Program Type").sum(numeric_only=True)
        st.bar_chart(allocation_summary)
    else:
        st.error("No optimal solution found.")

# Add a footer with the GitHub link
st.markdown("""
---
Explore the code on [GitHub](https://github.com/your-repo-link-here).
""")
