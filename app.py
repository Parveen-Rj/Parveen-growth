#streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project", page_icon="★")
st.title("Growth Mindset Challenge: Wed App with Streamlit")

st.header("Welcome to Your Growth Journey!")
st.write("Start your journey of learning and development from here.")

#qupite section
st.header("Today's Growth Mindset Quote")
st.write("“The only way to do great work is to love what you do.” – Steve Jobs")

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge yor're facing:")

#condition
if user_input:
    st.success(f"you're facing: {user_input}.keep pushing forwards towords your goal!")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Reflect on your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")

#acheivements
st.header("Celebrate Your Wins!")
acheivement = st.text_input("Share something you're recently accomplished:")

if acheivement:
    st.success(f"Amazing! You achieved: {acheivement}")
else:
    st.info("Big or small , every acheivement counts! Share one now")

#footer
st.write("- - -")
st.write("Keep believing in yourself. Growth is a Journey, not a destination!")
st.write("** Created by Parveen Malik**")


