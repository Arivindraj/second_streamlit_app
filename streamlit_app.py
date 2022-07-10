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

# Add a button to load the Connection Details
if st.button("Get Connection Details"):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = create_session_object()
  my_cnx.close()
  st.dataframe(my_data_rows)

def get_the_data():
  with my_cnx.cursor() as my_cur:
    #my_cur.execute("select current_warehouse(), current_database(), current_schema()")
    snow_df_co2 = my_cur.table("ENVIRONMENT.EDGARED2019").filter(col('Indicator Name') == 'Fossil CO2 Emissions').filter(col('Type Name') == 'All Type')
    snow_df_co2 = snow_df_co2.group_by('Location Name').agg(sum('$16').alias("Total CO2 Emissions")).filter(col('Location Name') != 'World').sort('Location Name')
    pd_df_co2  = snow_df_co2.to_pandas()
    return pd_df_co2.fetchall()
     
 # Add a button to load the Connection Details
if st.button("Get Data"):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data = get_the_data()
  my_cnx.close()
  st.dataframe(my_data)


# Add header and a subheader
st.header("Knoema: Environment Data Atlas")
st.subheader("Powered by Snowpark for Python and Snowflake Data Marketplace | Made with Streamlit")
