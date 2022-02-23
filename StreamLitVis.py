import streamlit as st
import pandas as pd
import altair as alt
# from gsheetsdb import connect
import chart
import base
# from google.oauth2 import service_account
# from googleapiclient.discovery import build


from shillelagh.backends.apsw.db import connect


# Create a connection object.
conn = connect()
sheet_url = st.secrets["public_gsheets_url"]

# connection = connect(":memory:")
# cursor = connection.cursor()

# query = "SELECT * FROM '{sheet_url}'"
# for row in cursor.execute(query):
#     print(row)
   
# def run_query(query): 




#THIS IS FETCHING THE DATA FROM THE GOOGLE SHEET USING SQL QUERY
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

rows = run_query(f'SELECT * FROM "{sheet_url}"')

#PAGE SET UP
st.title("Andover Compliment Page")


    
st.write("**Send a Compliment:**")
form = st.form("comment")
name = form.text_input("Compliment Recipient")
comment = form.text_area("Comment")
submit = form.form_submit_button("Add comment")

# if submit:
#     db.inset(conn, [[name, commen


#CAN MOSTLY IGNORE BELOW THIS

# # THIS IS HOW I LEARNED HOW TO SHOW THE ROWS
# for row in rows:
#     st.write(f"{row.name} has a :{row.pet}:")

#THIS LITTLE SECTION WILL ACTUALLY SHOW SMTH
# for row in rows:
#     st.table(rows)
