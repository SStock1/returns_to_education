"""
# author = Andy Banks
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")

# Data import

combined = pd.read_csv('combined.csv')

# Sidebar

st.sidebar.markdown('This is a prototype dashboard to present publicly available information on returns to education')
st.sidebar.markdown('The text and charts automatically update depending on the options chosen in the selection boxes.')
st.sidebar.markdown('You can find the source code [here](https://github.com/banksad/returns_to_education)')

# Page design
st.title('Returns to education')
            
# Qualification and provider selector
# -------------------------------------

# Inputs section

st.subheader('Earnings by provider, subject and sex')

st.markdown('This section examines the earnings of UK first degree graduates by provider, subject, and sex one, three and five years after graduation.')

st.markdown('Search for a product that you wish to analyse')

st.markdown('Search for a qualification you are interested in')

combined_product = st.selectbox('',set(list(combined['output product'])))