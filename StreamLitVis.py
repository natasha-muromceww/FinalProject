import streamlit as st
import pandas as pd
import altair as alt

from datetime import datetime
# from FinalProject import DataVisForm.png
from PIL import Image

# import matplotlib.pyplot as plt
# from wordcloud import WordCloud

# from gsheetsdb import connect
from shillelagh.backends.apsw.db import connect

#url: https://docs.google.com/spreadsheets/d/17bNU8T92Bu1OxNNvFMhVlkPtXw56hVSJlyXQhYxUwOw/edit?usp=sharing

#Page setup 
st.title("Live Poll PA")

image = Image.open('DataVisForm.png')
st.image(image, caption='Google Form QR Code')
   
#SHILLELAGH VERSION
connection = connect(":memory:")
cursor = connection.cursor()

query = """
SELECT * FROM "https://docs.google.com/spreadsheets/d/17bNU8T92Bu1OxNNvFMhVlkPtXw56hVSJlyXQhYxUwOw/edit?usp=sharing"
"""

data = []

for row in cursor.execute(query): #row is probs tuple 
   data.append(row)

df = pd.DataFrame(data, columns=['a', 'b', 'c', 'd'])
st.table(df)


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

    

