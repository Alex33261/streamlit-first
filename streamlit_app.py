import streamlit as st


st.title('To do list pour une reprise en douceur')

st.subheader('Guillaume')
st.write('This is some text.')
st.markdown(st.subheader("- LLM "))
st.markdown("- Item 2")
st.markdown("- Item 3")

message = st.chat_message("assistant")
message.write("Hello Guillaume")

st.divider()

st.subheader('Activite Souliman')
st.text('This is some text.')

st.divider()

st.subheader('Activite François')
st.text('This is some text.')
