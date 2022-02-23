import streamlit as st
import pandas as pd
import altair as alt
from gsheetsdb import connect


#Page setup 
st.title("Live Poll PA")



# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    row = conn.execute(query, headers=1)
    return row

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# # Print results.
# for row in rows:
#     st.table(rows)

for i in range(rows):
    new_row = run_query(f'SELECT * FROM "{sheet_url}"')
    st.table(new_row)
   
    

