import streamlit as st
import pandas as pd
import altair as alt

from datetime import datetime
from PIL import Image

#EMAIL IMPORT
import smtplib, ssl

#VISUALIZATIONS IMPORT
import plotly.graph_objects as go
import numpy as np

import matplotlib.pyplot as plt
from wordcloud import WordCloud

from shillelagh.backends.apsw.db import connect

#url: https://docs.google.com/spreadsheets/d/17bNU8T92Bu1OxNNvFMhVlkPtXw56hVSJlyXQhYxUwOw/edit?usp=sharing

#Page setup-----------------------------------------------------------
st.set_page_config(layout="wide")

#Top section layout
row1_1, row1_2 = st.columns((2,3))

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

df = pd.DataFrame(data, columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
#code check:
# st.table(df)


#SENDING COMPLIMENT FUNCTION-----------------------------------------------------------
# using import smtplib, ssl
   
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
  
#code check:
# send_compliment('nmuromcew22@andover.edu', 'email check')

# #SENDING EMAILS-----------------------------------------------------------
# # Uses st.cache to only rerun when the query changes or after 10 min.
# # @st.cache(ttl=600)
# the_datetime = datetime.now()
# # ten_minutes = datetime(0, 0, 0, 0, 10, 0, 0)
# # cache_time = run_datetime - ten_minutes

# st.write(the_datetime)
# # st.write(ten_minutes)
# # st.write(cache_time)


# for x in df.index:
#    st.write("in loop")
#    if df['a'][x] > 

#THIS WORKS FOR SENDING COMPLIMENTS IN A LOOP AND ACESSIGN PARTS IN A LOOP 
# for x in df.index:
#    st.write("hi1")
#    send_compliment(df['b'][x], df['c'][x])
#    st.write("hi")

# st.stop()
                   
#FIRST VISUALIZATION-----------------------------------------------------------
# import plotly.graph_objects as go
# import streamlit as st 
# import numpy as np


# desire = [1, 2, 3, 4, 8, 1, 4, 5, 6, 1]
# reception = [1, 2, 3, 4, 2, 9 , 3, 2 , 4, 5]
color_list = []
size_list = []
text_list = []

# for x in df.index:
#    (df['f'][x])

for x in df.index:
    color_list.append("rgb(252, " + str(-df['g'][x]/10 *(240-20) + 240) + ", 3)" )  
    size_list.append(50)
    text_list.append("desire rating: " + str(df['f'][x]) + " reception rating: " + str(df['g'][x]))
    
fig1 = go.Figure(data=[go.Scatter(
    x=desire, y=reception,
    text= text_list,
    mode='markers',
    marker=dict(
        color= color_list,
        size=size_list,
    )
)])

fig1.update_layout(
    title='Compliment Scatterplot',
    xaxis=dict(
        title='Desire for Compliments',
    ),
    yaxis=dict(
        title='Reception of Compliments',
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
)
#Test code:
# st.plotly_chart(fig, use_container_width=True)

#WORD CLOUD/SECOND VISUALIZATION-------------
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud
#my_list=["one", "one two", "three three three"]
st.set_option('deprecation.showPyplotGlobalUse', False)

adjective_list = df["d"].tolist()
#convert list to string and generate
unique_string=(" ").join(adjective_list)
wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
#plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
#code test:
# st.pyplot()

#THIRD VISUALIZATION-----------------------------------------------------------
compliment_categories = ["Humor", "Intelligence", "Athleticism", "Fashion", "Character", "Creativity", "Other"]
counts = [1, 2, 3, 4, 5, 6, 7]


fig = go.Figure([go.Bar(x = compliment_categories, y = counts)])


fig.update_layout(
    title='Compliments by Category',
    xaxis=dict(
        title='Compliment Types',
    ),
    yaxis=dict(
        title='Count',
    ),
    paper_bgcolor='rgb(242, 236, 218)',
    plot_bgcolor='rgb(232, 208, 137)',
)
#test code: 
# fig.show()

#VISUALIZATION LAYOUT-----------------------------------------------------------
row2_1, row2_2, row2_3 = st.columns((1, 1,1))

# compliment_list = df["b"].tolist()


with row2_1:
    st.write("**View Recent Compliments**")  
    for x in df.index:
        st.write(df['c'][x])

with row2_2:
    st.write("**First thing**")
    st.plotly_chart(fig1, use_container_width=True)
    
with row2_3:
    st.write("**Word Cloud**")
    st.pyplot()

row3_1, row3_2, row3_3 = st.columns((1,1, 1))

# with row3_1:
#     st.write(" ")

with row3_2:
    st.write("**Third thing**")
    fig.show()
 
with row3_3:
    st.write("**Fourth thing**")

