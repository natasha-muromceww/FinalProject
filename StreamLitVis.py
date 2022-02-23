import streamlit as st
import pandas as pd
import altair as alt

from shillelagh.backends.apsw.db import connect


connection = connect(":memory:")
cursor = connection.cursor()


query = """
SELECT * FROM "https://docs.google.com/spreadsheets/d/1v9jM22s_60OrW9O_fSHPQQa1VjV0MLJeg1rum9-UBco/edit?usp=sharing"
"""
for row in cursor.execute(query):
    st.write(row)
   
query = """
UPDATE "https://docs.google.com/spreadsheets/d/1v9jM22s_60OrW9O_fSHPQQa1VjV0MLJeg1rum9-UBco/edit?usp=sharing"
SET age = age + 1
WHERE name == 'Stacy'
"""

query = """
SELECT * FROM "https://docs.google.com/spreadsheets/d/1v9jM22s_60OrW9O_fSHPQQa1VjV0MLJeg1rum9-UBco/edit?usp=sharing"
"""
for row in cursor.execute(query):
    st.write(row)



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
