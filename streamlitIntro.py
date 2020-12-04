# Streamlit intro
# pip install streamlit
# Then do touch app.py this creates a new folder in your working directory
# streamlit --help
# streamlit run streamlitintro.py   # app.py or whatever you name it
import streamlit as st

# text/title
st.title("Streamlit Intro!")

# Header/Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# text
st.text("Hello Streamlit")

# Markdown
st.markdown("### This is markdown")

# Error/ Colorful text
st.success("Successful")
st.info("Information")
st.warning("This is a warning!")
st.error("This is an error!")
#st.exepiton("NameError('name three not defined')")
st.help(range)

st.write("Text with write")
st.write(range(10))

#images
from PIL import Image
img = Image.open("mlpic.jpg")
st.image(img,width=300,caption="Simple Image")

#videos.
vid_file = open("examplevid.mp4","rb").read()
#vid_bytes = vid_file.read()
st.video(vid_file)

# audio
#audio_file = open("examplemusic.mp3","rb").read()
#st.audio(audio_file,format='audio/mp3')


# widget check
# checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")

#Radio Buttons
status = st.radio("What is your status", ("Active","Inactive"))

if status == "Active":
    st.success("You are Active!")
else:
    st.warning("Inactive, Activate Now")

# SelectBox
occupation = st.selectbox("Your Occupation",["Programmer","Data Scientist","Analyst","Developer"])
st.write("You selected this option! ", occupation)

# MultiSelect
location = st.multiselect("where do you work?",("USA","Canada","Jamacia","Ausstrialia","Online","Nepal"))
st.write("You selected",len(location),"locations")


# Slider
level = st.slider("What is your level?",1,5)

# Buttons
st.button("Simple Button")
if st.button("About"):
    st.text("Streamlit is Cool")


# Text Input
firstname = st.text_input("Enter Your Firstname", "Type Here..")
if st.button("Submit"):
    result = firstname.title()
    st.success(result)


# Text Area
message = st.text_area("Enter Your message", "Type Here..")
if st.button(label ="Submit",key = "m_submit"):
    result2 = message.title()
    st.success(result2)

# date Input
import datetime
today = st.date_input("Today is", datetime.datetime.now())

#datetime
the_time = st.time_input("The time is", datetime.time())

# Displayying JSON
st.text("Display JSON")
st.json({'name':"Jesse","gender": "male"})

# Display Raw Code
st.text("Display Raw Code")
st.code("import numpy as np")

# Display Raw Code
with st.echo():
    #This will also show as comment
    import pandas as pd
    df = pd.DataFrame()

# Progress Subheader
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)



# Spinner
with st.spinner("Waiting...."):
    time.sleep(5)
st.success("Finsihed")

#Ballons
#st.balloons()


# Sidebars
st.sidebar.header("About")
st.sidebar.text("This is Streamlit tutorial")

#functions
@st.cache
def run_fxn():
    return range(100)

st.write(run_fxn())


# plot
st.pyplot()

# Dataframes
st.dataframes(df)

# tables
st.table(df)
