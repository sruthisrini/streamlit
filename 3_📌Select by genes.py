import pandas as pd
import plotly.express as px
from PIL import Image
import streamlit as st
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time
from streamlit_extras.switch_page_button import switch_page 
import subprocess

st.set_page_config(page_title="Database for cancer patients",layout='wide')
st.title("Potential splice sites mutations on exonic regions of cancer patients")
st.subheader("Multi-select by genes")
# Create an empty placeholder for the loading message
loading_placeholder = st.empty()

@st.cache_data
def data():
    data = "/Users/sruthisrinivasan/Documents/Files/sruthi_transcript.xlsx"
    df = pd.read_excel(data,dtype={'Position': str})
    return df

# When data is loaded, clear the loading message
df = data()
loading_placeholder.empty()

with st.form('input'):
        genes = df["Genes"].unique().tolist()
        department_selection = st.multiselect('Select by gene:', genes, default='TP53')
        submit_button = st.form_submit_button(label='Submit')
        start1 = time.time()

        if submit_button:
            mask = df['Genes'].isin(department_selection)
            st.subheader("****RESULTS****")
            st.dataframe(df[mask], hide_index=True)
            number_of_result = df[mask].shape[0]
            st.markdown(f'*Available Results: {number_of_result}*')
            bar = px.bar(df[mask], x='Splice_site', hover_data=['Genes'], color='Mutation', title="Distribution of mutations across different splice sites", color_continuous_scale=px.colors.sequential.Viridis, category_orders={"Mutation": ["A->C", "A->G", "A->T", "C->A", "C->G", "C->T", "G->A", "G->C", "G->T", "T->A", "T->C", "T->G"]})
            bar.update_xaxes(categoryorder='array', categoryarray= ['d3', 'd2', 'd1', 'a1', 'a2', 'a3'], showgrid=False)
            bar.update_yaxes(showgrid=False)
            st.plotly_chart(bar)
            plot = px.scatter(df[mask], y='Delta score - Donor Loss', x='PhastCons20way mammalian', color='LOEUF score cutoff', hover_data=['Genes'], labels={
                            "PhastCons20way mammalian": "Phastcons score"},
                        title="Comparison of SpliceAI prediction(Donor Loss) with Phastcons score")

            st.plotly_chart(plot)
            plot1 = px.scatter(df[mask], y='Delta score - Acceptor Loss', x='PhastCons20way mammalian', color='LOEUF score cutoff', hover_data=['Genes'], labels={
                            "PhastCons20way mammalian": "Phastcons score"},
                        title="Comparison of SpliceAI prediction(Acceptor Loss) with Phastcons score")

            st.plotly_chart(plot1)

            