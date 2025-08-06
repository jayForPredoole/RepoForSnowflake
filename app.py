import streamlit as st
import snowflake.connector

# App title
st.title("Minimal Streamlit App in Snowflake")

# Connect to Snowflake using the built-in connection
conn = st.experimental_connection("snowflake")

# Run a simple query
df = conn.query("SELECT CURRENT_DATE AS today, CURRENT_VERSION() AS version;")

# Display results
st.write("Snowflake Info:")
st.dataframe(df)