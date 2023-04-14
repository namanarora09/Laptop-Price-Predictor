import streamlit as st
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go

st.header(":red[Relation Between Laptop Price and Features]")

#resources path
FILE_DIR1=os.path.dirname(os.path.abspath(__file__))
FILE_DIR=os.path.join(FILE_DIR1,os.pardir)

#Load data
DATA_PATH=os.path.join(FILE_DIR,"laptop_price.csv")
df=pd.read_csv(DATA_PATH)
data=df.copy()
data.drop("MRP",axis=1,inplace=True)

feature=st.selectbox("Select Feature to see the Relation",(data.columns))

fig=px.box(df,x=feature,y='MRP',color=feature)
st.plotly_chart(fig,use_container_width=True)