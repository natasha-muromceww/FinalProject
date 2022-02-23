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
st.title("Live Poll PA")

image = Image.open('DataVisForm.png')
st.image(image, caption='Google Form QR Code')
   
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
   
# send_compliment('crhee24@andover.edu', 'i love you')

send_compliment('mdavis22@andover.edu', 'hi morgan u are amazing')
send_compliment('kaziabor22@andover.edu', 'hi kris you are beautiful')
send_compliment('cellis22@andover.edu', 'hi chenault you are beautiful')
send_compliment('cdesaintphalle22@andover.edu', 'hi Claire you are beautiful')


#THIS WORKS 
# for x in df.index:
#    st.write("hi1")
#    send_compliment(df['b'][x], df['c'][x])
#    st.write("hi")

st.stop()
                   
#VISUALIZATIONS--------------------------------------------------------------
#worldcloud

# # my_list=["one", "one two", "three three three"]


# #convert list to string and generate
# unique_string=(" ").join(data)
# wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
# plt.figure(figsize=(15,8))
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.savefig("your_file_name"+".png", bbox_inches='tight')
# plt.show()
# plt.close()

