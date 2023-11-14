import pandas as pd
import plotly.express as px
from PIL import Image
import streamlit as st
from time import sleep

st.set_page_config(page_title="About")
st.title("About")
splicing = Image.open("/Users/sruthisrinivasan/Desktop/Splicing.png")

st.markdown("Our database contains potential synonymous and non-synonymous mutations within splice sites of cancer patients (from COSMIC database). These mutations occur within exonic regions and can potentially influence splicing, particularly at the three nucleotides within the acceptor and donor arms. While these mutations are primarily predicted to be synonymous and non-synonymous, impacting the protein, they do not provide a direct assessment of their effect on splicing. However, it is possible that these mutations may indeed influence splicing events.")
st.image(image=splicing, caption="Impact of non-synonymous and synonymous mutations on splicing")
st.markdown("The database includes various columns, such as mutations, amino acid changes, splice site locations (3 from the acceptor end and 3 from the donor end), strand information, mutation type, and SpliceAI predictions.")