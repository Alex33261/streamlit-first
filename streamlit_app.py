import streamlit as st


st.title('To do list pour une reprise en douceur')

st.subheader('Guillaume')
st.markdown(st.subheader("- LLM "))
st.write('Comme tu le vois, on a découvert streamlit. A mon avis c est vraiment pas mal pour des petits formats d applis et je vois parfaitement ce genre de format pour le projet LLM')
st.markdown("- Item 2")
st.markdown("- Item 3")

message = st.chat_message("assistant")
message.write("Hello Guillaume")

st.divider()

st.subheader('Souliman')
st.text('This is some text.')

st.divider()

st.subheader('Activite François')
st.text('This is some text.')
