import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(1000000, 5),
     columns=['a', 'b', 'c','d','e'])

st.line_chart(chart_data)