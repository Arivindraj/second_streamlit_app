import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

st.set_page_config(
     page_title="Environment Data Atlas",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://developers.snowflake.com',
         'About': "This is an *extremely* cool app powered by Snowpark for Python, Streamlit, and Snowflake Data Marketplace"
     }
 )

 
streamlit.header("View Our Fruit List - Add Your Favorites!")
# Snowflake related function
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select top 100 * from ENVIRONMENT_DATA_ATLAS ")
    return my_cur.fetchall()
  
# Add a button to load the fruit
if streamlit.button("Get Fruit List"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
