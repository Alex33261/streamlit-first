import streamlit as st

[theme]
base="dark"
primaryColor="purple"

[theme]
font="Century Gothic"


st.title('Activite Guillaume')
st.subheader('A subheader with _italics_ :blue[colors] and emojis :sunglasses:')
st.text('This is some text.')

message = st.chat_message("assistant")
message.write("Hello Guillaume")

st.divider()

st.title('Activite Souliman')
st.subheader('A subheader with _italics_ :blue[colors] and emojis :sunglasses:')
st.text('This is some text.')

st.divider()

st.title('Activite François')
st.subheader('A subheader with _italics_ :blue[colors] and emojis :sunglasses:')
st.text('This is some text.')
