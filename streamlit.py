import streamlit as st

import pandas as pd
from numpy.random import default_rng as rng
df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.area_chart(df, x_label='areaX', y_label='areaY')
st.line_chart(df, x_label='lineX', y_label='lineY')
st.bar_chart(df, x_label='barX', y_label='barY')