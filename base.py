import streamlit as st
from PIL import Image

st.title("WELCOME TO YOUR INTERACTIVE HOME")
image = Image.open('welcomehome.jpg')
st.image(image)
st.header("Instructions")
st.write("This is the welcome page of your home. Use the emergent window on the left side to toggle between the different rooms avaliable. Inside of each yoom you will be able to control the lights and the door using your voice or the buttons.")
st.header("Have fun!")


