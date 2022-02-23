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
