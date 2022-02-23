import streamlit as st
import pandas as pd
from gsheetsdb import connect

# Create a connection object.
conn = connect()
sheet_url = st.secrets["public_gsheets_url"]

# rows1 = conn.execute(f'SELECT * FROM "{sheet_url}"')
# df1 = pd.DataFrame(rows1)
# st.write(df1)

# option = st.sidebar.selectbox('Select pet',df1.rows1)
# df1.set_index("pet", inplace = True)
# result = df1.loc[[option]]
# st.write(result)


# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

rows = run_query(f'SELECT * FROM "{sheet_url}"')

# # Print results.
# for row in rows:
#     st.write(f"{row.name} has a :{row.pet}:")

for row in rows:
    st.table(rows)
    
# st.write("**Add your own comment:**")
#     form = st.form("comment")
#     name = form.text_input("Name")
#     comment = form.text_area("Comment")
#     submit = form.form_submit_button("Add comment")

#     if submit:
# #         date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#         db.insert(conn, [[name, comment, date]])
# #         if "just_posted" not in st.session_state:
# #             st.session_state["just_posted"] = True
# #         st.experimental_rerun()
