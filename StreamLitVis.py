import streamlit as st
import pandas as pd
import altair as alt

from datetime import datetime
# from FinalProject import DataVisForm.png
from PIL import Image

#EMAIL IMPORT
import smtplib, ssl


# import matplotlib.pyplot as plt
# from wordcloud import WordCloud

# from gsheetsdb import connect
from shillelagh.backends.apsw.db import connect

#url: https://docs.google.com/spreadsheets/d/17bNU8T92Bu1OxNNvFMhVlkPtXw56hVSJlyXQhYxUwOw/edit?usp=sharing

#Page setup-----------------------------------------------------------
st.set_page_config(layout="wide")

#Top section layout
with row1_1:
    image = Image.open('DataVisForm.png')
    st.image(image, caption='Google Form QR Code')

with row1_2:
    st.title("Live Poll PA")
    st.write(
    """
    ##
    Fill out this survey to send compliments to your friends. 
    The compliments and additional data are visualized down below. 
    """)


   
#SHILLELAGH VERSION GRABBING DATA FROM SHEET -----------------------------------------------------
connection = connect(":memory:")
cursor = connection.cursor()

query = """
SELECT * FROM "https://docs.google.com/spreadsheets/d/17bNU8T92Bu1OxNNvFMhVlkPtXw56hVSJlyXQhYxUwOw/edit?usp=sharing"
"""

#USING QUERY TO MAKE DF -----------------------------------------------------------
data = []

for row in cursor.execute(query): #row is probs tuple 
   data.append(row)

df = pd.DataFrame(data, columns=['a', 'b', 'c', 'd'])
st.table(df)


#SENDING COMPLIMENT-----------------------------------------------------------
# import smtplib, ssl
   
def send_compliment(new_receiver_email, new_message):
   port = 465  # For SSL
   smtp_server = "smtp.gmail.com"
   sender_email = "andovercomplimentwall@gmail.com"  # Enter your address
   receiver_email = new_receiver_email  # Enter receiver address
   password = "cs630final"
   message = new_message
   context = ssl.create_default_context()
   with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)
   
# send_compliment('nmuromcew22@andover.edu', 'email check')

# Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
run_datetime = datetime.now()
ten_minutes = datetime(0, 0, 0, 0, 10, 0, 0)
cache_time = run_datetime - ten_minutes

st.write(datetime_object)
st.write(ten_minutes)
st.write(cache_time)

# for x in df.index:
#    st.write("in loop")
#    if df['a'][x] > 

#THIS WORKS 
# for x in df.index:
#    st.write("hi1")
#    send_compliment(df['b'][x], df['c'][x])
#    st.write("hi")

# st.stop()
                   

