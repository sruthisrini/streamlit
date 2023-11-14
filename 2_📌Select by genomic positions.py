
import pandas as pd
import plotly.express as px
from PIL import Image
import streamlit as st
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time
from streamlit_extras.switch_page_button import switch_page 
from st_pages import Page, show_pages, add_page_title




st.set_page_config(page_title="Database for cancer patients",layout='wide')
st.title("Potential splice sites mutations on exonic regions of cancer patients")
st.subheader("Select by genomic position")

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


col1, col2, col3,col4 = st.columns(4)

with col1:
    Gene = st.text_input("Gene:", value="A2M")

with col2:
    #Position = st.slider("Genomic position:",min_value=45442,max_value=248857830)
    Position=st.text_input("Genomic Position:",value=9074560)
with col3:
    Ref = st.text_input("Ref:", value="G")
with col4:
    Alt = st.text_input("Alt:", value="T")

if st.button("Submit"):
    # Filter the DataFrame based on the input values
    st.session_state["filtered_df"] = df[(df['Genes'] == Gene) & (df['Position'] == Position) & (df['Ref'] == Ref) & (df['Alt'] == Alt)]
    st.session_state["Gene"]=Gene
    st.session_state["Position"]=Position
    st.session_state["Ref"]=Ref
    st.session_state["Alt"]=Alt
    st.subheader("****RESULTS****")
    st.markdown("Database version-hg38")
    st.markdown(f"You searched by GENCODE gene symbol with name as **{st.session_state.Gene}**,Position as **{st.session_state.Position}** and Mutation as **{st.session_state.Ref}->{st.session_state.Alt}**")
    st.dataframe(st.session_state["filtered_df"],hide_index=True)





