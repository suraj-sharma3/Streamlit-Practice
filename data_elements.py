import streamlit as st
import pandas as pd

# Dataframe
st.header("Dataframe")

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10],
    'C': [11, 12, 13, 14, 15],
    'D': [16, 17, 18, 19, 20],
    'E': [21, 22, 23, 24, 25]
}

df = pd.DataFrame(data)

st.dataframe(df) # provides the download, maximize and search option by default, you can also sort the data in a column by clicking on the column name

# Editable dataframe
st.header("Editable Dataframe")
editable_df = st.data_editor(df)
# print(editable_df) # to print the df edited on the UI in the terminal, whenever you make a change in the df, the entire script re runs

# Static Table
st.header("Static Table")
st.table(df)

# Metrics
st.subheader("Metrics")
st.metric(label="Total Rows : ", value=len(df))
st.metric(label="Average C : ", value=round(df['C'].mean(), 1))

# JSON and Dictionary
st.subheader("JSON and Dictionary")
sample_json = {
    "id": 1,
    "name": "Alice Smith",
    "email": "alice@example.com",
    "age": 28,
    "is_active": True
}
st.json(sample_json)

st.write("Sample JSON as Dictionary : ", sample_json)



