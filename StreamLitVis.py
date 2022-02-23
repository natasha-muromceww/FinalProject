import streamlit as st
import pandas as pd
import altair as alt
# import time

# from shillelagh.backends.apsw.db import connect

# connection = connect(":memory:")
# cursor = connection.cursor()


# query = """
# SELECT * FROM "https://docs.google.com/spreadsheets/d/1v9jM22s_60OrW9O_fSHPQQa1VjV0MLJeg1rum9-UBco/edit?usp=sharing"
# """
# for row in cursor.execute(query):
#     st.write(row)
   
# query = """
# UPDATE "https://docs.google.com/spreadsheets/d/1v9jM22s_60OrW9O_fSHPQQa1VjV0MLJeg1rum9-UBco/edit?usp=sharing"
# SET age = 10
# WHERE name == 'Chris'
# """

# # time.sleep(1)

# query = """
# SELECT * FROM "https://docs.google.com/spreadsheets/d/1v9jM22s_60OrW9O_fSHPQQa1VjV0MLJeg1rum9-UBco/edit?usp=sharing"
# """
# for row in cursor.execute(query):
#     st.write(row)

data = {'recipient': ['Natasha'], 'compliment': ['Hii']}
chart = st.table(data)
# df = pd.DataFrame(data)
# st.write(df)

def add_row(recipient, compliment):
   new_row = {'recipient': [recipient], 'compliment': [compliment]}
   chart.add_rows(new_row)
   return chart

#PAGE SET UP
st.title("Andover Compliment Page")

st.write("**Send a Compliment:**")
form = st.form("comment")
recipient = form.text_input("Compliment Recipient")
compliment = form.text_area("Compliment")
submit = form.form_submit_button("Add comment")

if submit:
   add_row(recipient, compliment)
   
   
   
#    data1 = {'recipient': [recipient], 'compliment': [compliment]}
#    chart.add_rows({'recipient': [recipient], 'compliment': [compliment]})
#    data1 = {'recipient': [recipient], 'compliment': [compliment]}
#    chart.add_rows(data1)


