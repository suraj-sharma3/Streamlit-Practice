# pip install streamlit numpy pandas matplotlib
# Run streamlit app with command "streamlit run pythonfilename.py"
# streamlit supports hot reloading i.e, the changes made in the code are updated and we just have to refresh the streamlit app on our browser and the changes will be reflected
# select the always rerun option on the streamlit app so that you don't even have to refresh to see the changes
# So enable autosave in VS code and select always rerun option on the streamlit app and the changes made in the code will automatically reflect in the app

import streamlit as st

st.write("Hello Universe!")
# st.write can write text, number or any python object like a dictionary or a pandas dataframe on the user interface

my_dict = {'Name' : "Suraj", "Last name" : "Sharma"}
st.write(my_dict)

# Even this text that you write outsude the st.write function gets displayed on the UI
3 + 10 # answer of this will be printed

"Hi My name is Suraj"

flag = True

"hello streamlit" if flag else "Bye Streamlit" # output of this will also be visible on the UI

# Whenever you do any change in the streamlit UI file, streamlit runs the entire file from top to bottom

# whenever any event occurs on the streamlit UI that changes the state of the streamlit app, the entire code is re run from top to bottom

pressed = st.button("Click Me")

pressed

second_button = st.button("Second Button")

st.write(f"Second Button : {second_button}")

# No matter how small is the change or event that occurs on the UI, whenever a change or an event occurs, streamlit re runs the entire script

