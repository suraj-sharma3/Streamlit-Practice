import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.header("Charts")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
# np.random.randn(20, 3) returns a 2D NumPy array (a matrix) with 20 rows and 3 columns

# features like zoom, download, etc are already built in for the charts created with streamlit
st.subheader("Area Chart")
st.area_chart(chart_data) 

st.subheader("Bar Chart")
st.bar_chart(chart_data)

st.subheader("Line Chart")
st.line_chart(chart_data)

# data for scatter chart
st.subheader("Scatter Chart")
scatter_plot_data = pd.DataFrame(
    {
        'x' : np.random.randn(100), # This line generates 100 random numbers
        'y' : np.random.randn(100)
    }
)
st.scatter_chart(scatter_plot_data)

# Map
data = pd.DataFrame({
    'lat': np.random.randn(100) * 0.01 + 37.76,
    'lon': np.random.randn(100) * 0.01 - 122.4
})

st.map(data)

# PyPlot Chart

st.subheader("PyPlot Chart")
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label = 'A')
ax.plot(chart_data['B'], label = 'B')
ax.plot(chart_data['C'], label = 'C')
ax.set_title("PyPlot Line Chart")
ax.legend()
st.pyplot(fig)