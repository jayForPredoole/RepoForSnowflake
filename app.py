import streamlit as st
from snowflake.snowpark.context import get_active_session

# App title
st.title("Minimal Streamlit App in Snowflake")

# Get the active Snowflake session
session = get_active_session()

# Run a simple query
df = session.sql("SELECT CURRENT_DATE AS today, CURRENT_VERSION() AS version").to_pandas()

# Display results
st.write("Snowflake Info:")
st.dataframe(df)