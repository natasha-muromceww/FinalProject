import streamlit as st
import pandas as pd
import altair as alt

from shillelagh.backends.apsw.db import connect

sheet_url = st.secrets["public_gsheets_url"]


connection = connect(":memory:")
cursor = connection.cursor()

query = "SELECT * FROM '{sheet_url}'"
for row in cursor.execute(query):
    st.write(row)
   

# if __name__ == "__main__":
#     connection = connect(":memory:")
#     cursor = connection.cursor()

#     SQL = """
#     SELECT *
#     FROM "https://docs.google.com/spreadsheets/d/1v9jM22s_60OrW9O_fSHPQQa1VjV0MLJeg1rum9-UBco/edit?usp=sharing"
#     """
#     for row in cursor.execute(SQL):
#         st.write(row)

# SELECT name, SUM(age)
# FROM "https://docs.google.com/spreadsheets/d/1v9jM22s_60OrW9O_fSHPQQa1VjV0MLJeg1rum9-UBco/edit?usp=sharing"
# WHERE age > 0
# # GROUP BY country

# UPDATE "https://docs.google.com/spreadsheets/d/1v9jM22s_60OrW9O_fSHPQQa1VjV0MLJeg1rum9-UBco/edit?usp=sharing"
# SET cnt = cnt + 1
# WHERE name == 'Stacy'



#THIS IS FETCHING THE DATA FROM THE GOOGLE SHEET USING SQL QUERY
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
# def run_query(query):
#     rows = conn.execute(query, headers=1)
#     return rows

# rows = run_query(f'SELECT * FROM "{sheet_url}"')

#PAGE SET UP
st.title("Andover Compliment Page")

st.write("**Send a Compliment:**")
form = st.form("comment")
name = form.text_input("Compliment Recipient")
comment = form.text_area("Comment")
submit = form.form_submit_button("Add comment")

# if submit:
#    UPDATE sheet_url
#    SET 
