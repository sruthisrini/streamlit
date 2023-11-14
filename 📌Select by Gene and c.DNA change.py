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
st.header("Select by gene and c.DNA change")

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


col1, col2 = st.columns(2)
#options = st.radio('Selection of exonic variants', ['Select by gene and c.DNA change', 'Select by genomic position'])

with col1:
    Gene = st.text_input("Gene:", value="A2M")

with col2:
    DNA = st.text_input("c.DNA:", value="c.G2468A")

if st.button("Submit"):
    # Filter the DataFrame based on the input values
    st.session_state["filtered_df"] = df[(df['Genes'] == Gene) & (df['c.DNA change'] == DNA)]
    st.session_state["Gene"]=Gene
    st.session_state["DNA"]=DNA
    st.subheader("****RESULTS****")
    st.markdown("Database version-hg38")
    st.markdown(f"You searched by GENCODE gene symbol with name as **{st.session_state.Gene}** and c.DNA as **{st.session_state.DNA}**")
    st.dataframe(st.session_state["filtered_df"],hide_index=True)
        # Set session state to indicate a page transition
        #switch_page("Results")

    

