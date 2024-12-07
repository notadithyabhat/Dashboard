import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import gurobipy as gp
from gurobipy import GRB
import tempfile
import altair as alt

# Set up the page configuration
st.set_page_config(page_title="Equipment Allocation Optimization", layout="wide")

# Database connection setup
try:
    # Aiven server credentials
    DB_USER = st.secrets["database"]["DB_USER"]
    DB_PASS = st.secrets["database"]["DB_PASS"]
    DB_HOST = st.secrets["database"]["DB_HOST"]
    DB_PORT = st.secrets["database"]["DB_PORT"]
    DB_NAME = st.secrets["database"]["DB_NAME"]
    ssl_ca = st.secrets["database"]["SSL_CA"]

    # Create a temporary file for the SSL certificate
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pem') as temp_file:
        temp_file.write(ssl_ca.encode('utf-8'))  # Write the certificate content
        SSL_CA_PATH = temp_file.name  # Save the temporary file path

    # Create the database engine with SSL enabled
    engine = create_engine(
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?ssl_ca={SSL_CA_PATH}"
    )

    # Test the connection
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    st.success("Connected to the Aiven database successfully!")
except Exception as e:
    st.error(f"Error connecting to the Aiven database: {e}")
    st.stop()

# Page title and introduction
st.title("Optimization: Equipment Allocation")

st.markdown("""
## Overview
Welcome to the Equipment Allocation Dashboard! This platform helps you maximize the usage of equipment across different program types efficiently. 

### Key Highlights:
- **Purpose**: Optimize equipment allocation to enhance resource utilization.
- **Constraints**:
    - Each piece of equipment is assigned to one program.
    - Program and equipment capacities are respected.

🔍 Dive into the data and optimization results below!
""")

# Query to fetch equipment usage data
@st.cache_data
def fetch_equipment_data():
    query = """
    SELECT
        VE.Type AS Equipment_Type,
        VE.Name AS Equipment_Name,
        SUM(WSE.Equipment_ID) AS Usage_Count
    FROM
        Workout_Session_Uses_Equipment WSE
    JOIN
        VR_Equipment VE
    ON
        WSE.Equipment_ID = VE.Equipment_ID
    GROUP BY
        VE.Type, VE.Name
    ORDER BY
        Usage_Count DESC;
    """
    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df

# Fetch the data
equipment_data = fetch_equipment_data()

# Display key metrics
st.markdown("### Key Metrics")
total_equipment = equipment_data["Equipment_Name"].nunique()
total_usage = equipment_data["Usage_Count"].sum()
st.metric("Total Equipment", total_equipment)
st.metric("Total Usage Count", total_usage)

# Display equipment usage data
st.markdown("### Equipment Usage Data")
st.dataframe(equipment_data, use_container_width=True)
st.caption("🔽 Filter and sort equipment usage data for better insights.")

# Optimization logic
if not equipment_data.empty:
    try:
        # Prepare the data
        equipment_names = equipment_data["Equipment_Name"].tolist()
        usage_counts = {row["Equipment_Name"]: row["Usage_Count"] for _, row in equipment_data.iterrows()}
        
        # Dummy program types for optimization (replace with real program types if available)
        program_types = [f"Program_{i}" for i in range(1, 6)]  # Example program types

        # Gurobi model
        model = gp.Model("Equipment Allocation")

        # Decision variables: binary variables indicating if equipment j is used for program i
        x = model.addVars(program_types, equipment_names, vtype=GRB.BINARY, name="x")

        # Objective: Maximize usage counts
        model.setObjective(
            gp.quicksum(x[i, j] * usage_counts[j] for i in program_types for j in equipment_names),
            GRB.MAXIMIZE
        )

        # Constraints
        # Equipment availability constraint
        for j in equipment_names:
            model.addConstr(
                gp.quicksum(x[i, j] for i in program_types) <= 1,
                name=f"Equipment_Availability_{j}"
            )

        # Program type capacity constraint
        for i in program_types:
            model.addConstr(
                gp.quicksum(x[i, j] for j in equipment_names) <= len(equipment_names),
                name=f"Program_Capacity_{i}"
            )

        # Optimize the model
        model.optimize()

        # Display the results
        if model.status == GRB.OPTIMAL:
            st.markdown("### Optimal Equipment Allocation Results")
            results = []
            for i in program_types:
                for j in equipment_names:
                    if x[i, j].x > 0.5:  # Allocated equipment
                        results.append({"Program Type": i, "Equipment": j, "Usage Count": usage_counts[j]})

            # Display results as a DataFrame
            results_df = pd.DataFrame(results)
            st.table(results_df)

            # Visualization: Equipment Usage Distribution
            equipment_dist = equipment_data.groupby("Equipment_Type")["Usage_Count"].sum().reset_index()
            pie_chart = alt.Chart(equipment_dist).mark_arc().encode(
                theta=alt.Theta("Usage_Count:Q", title="Usage Count"),
                color=alt.Color("Equipment_Type:N", title="Equipment Type"),
                tooltip=["Equipment_Type", "Usage_Count"]
            ).properties(title="Equipment Usage Distribution")
            st.altair_chart(pie_chart, use_container_width=True)

        else:
            st.error("No optimal solution found.")

    except Exception as e:
        st.error(f"Error during optimization: {e}")

# Conclusion section
st.markdown("""
## Conclusion
- The optimization model effectively allocates equipment to maximize usage.
- Insights like equipment distribution and program-specific allocation help in planning.

📈 Use this analysis to strategize resource management and improve operational efficiency!
""")
