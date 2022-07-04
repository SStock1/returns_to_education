"""
# author = Andy Banks
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

# Data import

data = pd.read_csv('cleaned.csv')

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

qualification = st.selectbox('Search for a qualification you are interested in',set(list(data['subject_name'])))

data_q = data[data['subject_name']==qualification]

provider = st.selectbox('Search for an education provider',set(list(data_q['provider_name'])))

data_qp = data_q[data_q['provider_name']==provider]

sex = st.selectbox('Choose sex of graduate',set(list(data_qp['sex'])))

data_qps = data_qp[data_qp['sex']==sex]

if len(data_qps)==0:

    st.markdown('Selection not available')

else:

    fig = px.bar(data_qps, x='YAG', y=['earnigs_LQ','earnings_median','earnings_UQ'], labels={'YAG':'Years after graduation'}, barmode='group')

    fig.update_layout(title='Earnings after graduation')

    fig.update_xaxes(tickvals=sorted(list(data_qps['YAG'].values)))

    st.plotly_chart(fig, use_container_width=True)