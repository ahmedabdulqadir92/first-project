
import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly.express as px 

st.set_page_config(page_title='dummy ',layout='wide')
st.title('dummy dashboard')

df=px.data.tips()

page=st.radio('choose an option',['navigate','dashboard','reports'])


st.sidebar.header('Filters')
selected_day=st.sidebar.selectbox('select day',df['day'].unique())
selected_time=st.sidebar.radio('select time',df['time'].unique())
selected_gender=st.sidebar.multiselect('select a gender',df['sex'].unique())

min_bill,max_bill=st.sidebar.slider('total_bill_range',
                                    float(df['total_bill'].min()),
                                    float(df['total_bill'].max()),
                                    (float(df['total_bill'].min()),float(df['total_bill'].max())))

min_tip,max_tip=st.sidebar.slider('total_tip_range',
                                    float(df['tip'].min()),
                                    float(df['tip'].max()),
                                    (float(df['tip'].min()),float(df['tip'].max())))
filtered_df=df

filtered_df=filtered_df[(filtered_df['day']==selected_day)&(filtered_df['time']==selected_time)&
                        (filtered_df['total_bill'].between(min_bill,max_bill))&
                        (filtered_df['tip'].between(min_tip,max_tip))]

if selected_gender:
    filtered_df=filtered_df[filtered_df['sex'].isin(selected_gender)]

if page =='navigate':
    st.subheader('work in progress')
elif page =='dashboard':

    tab1,tab2 =st.tabs(['kpis','visuals'])

    with tab1:
        st.dataframe(filtered_df)

        col1,col2=st.columns(2,gap='large')

        col1.metric('total records',len(filtered_df))
        col2.metric('average bill',filtered_df['total_bill'].mean())


    with tab2:
        st.subheader('visuals')

        col3,col4=st.columns(2,gap='large')

        with col3:
            fig1=px.histogram(filtered_df,x='total_bill') 
            st.plotly_chart(fig1,use_container_width=True)

        with col4:
            fig2=px.histogram(filtered_df,x='total_bill')
            st.plotly_chart(fig2,use_container_width=True) 

else:
    st.subheader('work in progress')



