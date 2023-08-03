import streamlit as st


st.title('Activite Guillaume')
st.subheader('To-do list pour une reprise en douceur')
st.write('This is some text.')
st.markdown(st.subheader("- LLM "))
st.markdown("- Item 2")
st.markdown("- Item 3")

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
