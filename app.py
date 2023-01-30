import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide")
final_df=pd.read_csv("india.csv")
List_of_states=list(final_df["State"].unique())
List_of_states.insert(0,"Entire India")

st.sidebar.title("India's Data Visualization")
Selected_States = st.sidebar.selectbox("select a state",List_of_states)
Primary = st.sidebar.selectbox("select first Category",sorted(final_df.columns[5:]))
Secondary = st.sidebar.selectbox("select second Category",sorted(final_df.columns[5:]))
plot = st.sidebar.button("Plot Graph")

if plot:
    st.text("Size of point represent primary_first category")
    st.text("Color of point represent primary_first category")
    if Selected_States == "Entire India":
        fig = px.scatter_mapbox(final_df, lat="Latitude", lon="Longitude",size=Primary,color=Secondary, zoom=4,size_max=35,
                                mapbox_style="carto-positron",width=1500,height=900,hover_name="District",
                                color_continuous_scale=px.colors.sequential.Rainbow)
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = final_df[final_df["State"] == Selected_States]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=Primary, color=Secondary, zoom=6,
                                size_max=35,color_continuous_scale=px.colors.sequential.Viridis,
                                mapbox_style="carto-positron", width=1500, height=900,hover_name="District")
        st.plotly_chart(fig, use_container_width=True)