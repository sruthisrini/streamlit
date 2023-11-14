

#st.set_page_config(page_title="About")
#st.title("The potential synonymous and non-synonymous mutations impacting splicing in COSMIC database")


import pandas as pd
import plotly.express as px
from PIL import Image
import streamlit as st
from time import sleep

st.set_page_config(page_title="Experimentally verified",layout='wide')
st.title("Splicing impact on experimentally validated synonymous and non-synonymous mutations")
#st.sidebar.success("Select a page below")


data="/Users/sruthisrinivasan/Downloads/Splicing mutations.xlsx"
df=pd.read_excel(data)


with st.form('input'):
    df=pd.read_excel(data,dtype={'Position': str})

    genes=df["Gene"].unique().tolist()
    department_selection = st.multiselect('Select by gene:',genes)
    #mask=df['Genes'].isin(department_selection)
    #st.write('You selected:', st.dataframe(df[mask],hide_index=True))
    #number_of_result = df[mask].shape[0]
    #st.markdown(f'*Available Results: {number_of_result}*')

    submit_button = st.form_submit_button(label='Submit')


if submit_button:
    mask=df['Gene'].isin(department_selection)
    st.subheader("****RESULTS****")
    #st.write('You selected: {}'.format(df[mask]))
    selected_data = df[mask]
    st.dataframe(df[mask],hide_index=True)
    number_of_result = df[mask].shape[0]
    st.markdown(f'*Available Results: {number_of_result}*')
    bar = px.bar(df[mask],y='Gene',color='Splice site',title="Distribution of splice site across genes",color_continuous_scale=px.colors.sequential.Viridis,orientation='h',category_orders={"Splice site": ['d3','d2','d1','a1','a2','a3']})
    
    st.plotly_chart(bar)
    
        

