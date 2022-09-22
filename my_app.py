

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Text / Title
st.title("Streamlit Tutorials")

# Header / Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Normal Text
st.text("Hello Streamlit")

# Markdown
st.markdown("# This is first markdown")
st.markdown("## This is second markdown")
st.markdown("### This is third markdown")
st.markdown("*This is an italic text*")
st.markdown("Markdown elimizi klavyeden kaldırmadan yazı yazmamızı sağlar.")
st.markdown("- First")

#  Error/colorful Text
st.success("Succesful")

st.info("Information")

st.warning("This is a warning")

st.error("This is an error Danger")

st.exception("NameError('name three not defined')")

# Get Help Info About Python
st.help(range)
st.success(st.help(range))

#Writing Text Super Fxn
st.write("Text with write")
st.write(range(10))
st.write(zip())
st.write(int(3))

# Images
img = Image.open("images.jpeg")
st.image(img, caption= "So cute")
st.image(img,width=300,caption="Adorable")

# Videos
st.video("https://www.youtube.com/watch?v=jHWKtQHXVJg")

# saved videos
#vid_file = open("example.mp4","rb").read()
# vid_bytes = vid_file.read()
#st.video(vid_file)

# Widget
# Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")
else:
    st.text("...")

# Radio Button
status = st.radio("What is your status?",("Active", "Inactive"))
if status == "Active":
    st.success("You are active")
else:
    st.warning("Inactive, Activate")

answer = st.radio("Which one is your degree?",("Bachelor", "Master","Ph.D"))
if answer == "Bachelor":
    st.success("Bachelor")
elif answer =="Master":
    st.warning("Master")
else:
    st.info("Ph.D")

# Select Box
occupation = st.selectbox("Your Occupation",["Programmer","Data Scientist","Businessman"])
st.write("Your selected this option",occupation)

# Multiselect
location = st.multiselect("Where do you work?",("London","New York", "Accra", "Kiev"))
if len(location) == 1:
    st.write("Your location is", location[0])
elif len(location) == 2:
    st.write("Your locations are", location[0], "and",location[1])
# else:
#     for i in range(len(location)):
#         st.write("Your locations are ", location[i])
#         st.write(",")

# Slider
level = st.slider("What is your level",1,15)
st.write("Your level is",level)

# Buttons
st.button("Simple Button")

if st.button("About"):
    st.text("Streamlit is cool")

# Text Input
firstname =st.text_input("Enter Your Firstname","Type Here ...")
if st.button("Submit"):
    result = firstname.title()
    st.success(result)

# Text Area
message =st.text_area("Enter Your message","Type Here ...")
if st.button("Sub"):
    result = message.title()
    st.success(result)

# Date Input
name = st.text_input("Enter Your name","Type Here ...")
sonuc = st.write("Your name is",name)








