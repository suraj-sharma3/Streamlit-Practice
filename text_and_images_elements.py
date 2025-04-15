import streamlit as st
import os

# text elements

st.title("Main heading")
st.header("Heading")
st.subheader("Sub Heading")
st.markdown("# Heading level 1 in markdown")
st.caption("This is caption")

code_snippet = """
def add_num(num1, num2):
    ans = num1 + num2
    return ans
"""

st.code(code_snippet, language="python")

st.divider() # puts a horizontal line on the UI

# images

# put your images in a folder named static (don't name the folder anything else), the static folder should be in the same directory as your streamlit UI script

st.image(os.path.join(os.getcwd(), 'static', 'city-7359472.jpg')) # you'll also get an option to display the image in full screen on the UI
