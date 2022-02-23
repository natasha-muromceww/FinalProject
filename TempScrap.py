# from gsheetsdb import connect
# import chart
# import base
# from google.oauth2 import service_account
# from googleapiclient.discovery import build


#CAN MOSTLY IGNORE BELOW THIS

# # THIS IS HOW I LEARNED HOW TO SHOW THE ROWS
# for row in rows:
#     st.write(f"{row.name} has a :{row.pet}:")

#THIS LITTLE SECTION WILL ACTUALLY SHOW SMTH
# for row in rows:
#     st.table(rows)

# google_sheet = "https://docs.google.com/spreadsheets/d/1v9jM22s_60OrW9O_fSHPQQa1VjV0MLJeg1rum9-UBco/edit?usp=sharing"

# Create a connection object.
# conn = connect()
# sheet_url = st.secrets["public_gsheets_url"]


# if __name__ == "__main__":
#     connection = connect(":memory:")
#     cursor = connection.cursor()

#     SQL = """
#     SELECT *
#     FROM "https://docs.google.com/spreadsheets/d/1v9jM22s_60OrW9O_fSHPQQa1VjV0MLJeg1rum9-UBco/edit?usp=sharing"
#     """
#     for row in cursor.execute(SQL):
#         st.write(row)


#THIS IS FETCHING THE DATA FROM THE GOOGLE SHEET USING SQL QUERY
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
# def run_query(query):
#     rows = conn.execute(query, headers=1)
#     return rows

# rows = run_query(f'SELECT * FROM "{sheet_url}"')

# SELECT name, SUM(age)
# FROM "https://docs.google.com/spreadsheets/d/1v9jM22s_60OrW9O_fSHPQQa1VjV0MLJeg1rum9-UBco/edit?usp=sharing"
# WHERE age > 0
# # GROUP BY country


# import time

# from shillelagh.backends.apsw.db import connect

# url: https://docs.google.com/spreadsheets/d/17bNU8T92Bu1OxNNvFMhVlkPtXw56hVSJlyXQhYxUwOw/edit?usp=sharing

# connection = connect(":memory:")
# cursor = connection.cursor()

# #Create a connection object.
# conn = connect()
# sheet_url = st.secrets["public_gsheets_url"]

# df1 = pd.DataFrame()
# my_table = st.table(df1)

# query = """
# SELECT * FROM "https://docs.google.com/spreadsheets/d/17bNU8T92Bu1OxNNvFMhVlkPtXw56hVSJlyXQhYxUwOw/edit?usp=sharing"
# """
# for row in cursor.execute(query):
#     my_table.add_rows(row)

# st.write(my_table)

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

# data = {'recipient': ['Natasha'], 'compliment': ['Hii']}
# chart = st.table(data)
# # df = pd.DataFrame(data)
# # st.write(df)

# def add_row(recipient, compliment):
#    new_row = {'recipient': [recipient], 'compliment': [compliment]}
#    chart.add_rows(new_row)
#    return chart

#PAGE SET UP
# st.title("Andover Compliment Page")

# st.write("**Send a Compliment:**")
# form = st.form("comment")
# recipient = form.text_input("Compliment Recipient")
# compliment = form.text_area("Compliment")
# submit = form.form_submit_button("Add comment")

# if submit:
#    add_row(recipient, compliment)
   
   
   
#    data1 = {'recipient': [recipient], 'compliment': [compliment]}
#    chart.add_rows({'recipient': [recipient], 'compliment': [compliment]})
#    data1 = {'recipient': [recipient], 'compliment': [compliment]}
#    chart.add_rows(data1)


#CODE NOTES: you left off trying to append enw data to the chart

# data = {'a': [], 'b': [], 'c': []}
# df = pd.DataFrame(data)

# for row in cursor.execute(query):
#     df.append(row)

# st.table(df)

# #GSHEETS VERSION
# # Create a connection object.
# conn = connect()

# # Perform SQL query on the Google Sheet.
# # Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
# def run_query(query):
#     row = conn.execute(query, headers=1)
#     return row

# sheet_url = st.secrets["public_gsheets_url"]
# rows = run_query(f'SELECT * FROM "{sheet_url}"')

# # # Print results.
# # for row in rows:
# #     st.table(rows)

# for i in range(rows):
#     new_row = run_query(f'SELECT * FROM "{sheet_url}"')
#     st.table(new_row)

# altair
# vega-datasets
# google-api-python-client
# google-auth
# google-auth-httplib2
# protobuf
