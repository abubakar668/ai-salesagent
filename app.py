import streamlit as st
from model import call_groq_model

st.title('Sales Assistant Prototype')

product_name = st.text_input('Product Name')
company_url = st.text_input('Company URL')
product_category = st.text_input('Product Category')
competitors = st.text_area('Competitors URLs (comma-separated)')
value_proposition = st.text_input('Value Proposition')
target_customer = st.text_input('Target Customer')
file_upload = st.file_uploader('Upload product overview sheet or deck', type=['pdf', 'docx', 'pptx'])

submit_button = st.button('Generate Insights')

if submit_button:
    insights = call_groq_model(product_name, company_url, product_category, competitors, value_proposition, target_customer)
    if insights:
        st.subheader('Generated Insights')
        st.write(insights)
    else:
        st.error("No insights were generated. Please check the inputs and try again.")