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

# Add header and a subheader
    st.header("Knoema: Environment Data Atlas")
    st.subheader("Powered by Snowpark for Python and Snowflake Data Marketplace | Made with Streamlit")
    


     
