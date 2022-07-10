import streamlit as st
import pandas as pd
import requests

# Snowpark
#from snowflake.snowpark.session import Session
#from snowflake.snowpark.functions import avg, sum, col,lit
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

# Create Session object
def create_session_object():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select current_warehouse(), current_database(), current_schema()")
    return my_cur.fetchall()

# Add a button to load teh fruit
if st.button("Get Fruit List"):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = create_session_object()
  my_cnx.close()
  st.dataframe(my_data_rows)

# Add header and a subheader
st.header("Knoema: Environment Data Atlas")
st.subheader("Powered by Snowpark for Python and Snowflake Data Marketplace | Made with Streamlit")
