import streamlit as st
import pandas as pd
# Set page configuration
st.set_page_config(
    page_title="IOE Aggregate Percentage Calculator",
    page_icon="📊"
)


st.title('IOE Aggregate Percentage Calculator for BEI')



x1 = st.number_input('Enter your 1st Sem Grand Total', value= 0)
x2 = st.number_input('Enter your 2nd Sem Grand Total', value= 0)
x3 = st.number_input('Enter your 3rd Sem Grand Total', value= 0)
x4 = st.number_input('Enter your 4th Sem Grand Total', value= 0)
x5 = st.number_input('Enter your 5th Sem Grand Total', value= 0)
x6 = st.number_input('Enter your 6th Sem Grand Total', value= 0)
x7 = st.number_input('Enter your 7th Sem Grand Total', value= 0)
x8 = st.number_input('Enter your 8th Sem Grand Total', value= 0)


operation = st.button('Submit')
if operation:
    result = ((x1*10)/775)+((x2*10)/725)+((x3*10)/700)+((x4*10)/775)+((x5*15)/775)+((x6*15)/825)+((x7*15)/750)+((x8*15)/825)
    result1 = round(result, 3)
    if result1 >= 80.0:
        st.markdown(f'#### Congratulations! You have achieved Distinction. Your Aggregate Percentage is {result1}%')
    elif 65.0 <= result1 < 80.0:
        st.markdown(f'#### Congratulations! You have achieved First Division. Your Aggregate Percentage is {result1}%')
    elif 50.0 <= result1 < 65.0:
        st.markdown(f'#### Congratulations! You have achieved Second Division. Your Aggregate Percentage is {result1}%')
    elif 40.0 <= result1 < 50.0:
        st.markdown(f'#### Congratulations! You have passed. Your Aggregate Percentage is {result1}%')
    else:
        st.markdown(f'#### Sorry to inform you that you have not passed! Your Aggregate Percentage is {result1}%')



