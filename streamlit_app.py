import streamlit as st

st.image('streamlit-first/GuillaumeSourireMagique.png')
st.title('To do list pour une reprise en douceur')

st.subheader('Guillaume')
message = st.chat_message("assistant")
message.write("Hello Guillaume, alors ces vacances ? Pas trop chaud ?")

st.markdown(st.subheader("- LLM "))
st.write('Comme tu le vois, on a découvert streamlit. A mon avis c est vraiment pas mal pour des petits formats d applis et je vois parfaitement ce genre de format pour le projet LLM. Tu peux aussi deployer des applis avec HuggingFace en streamlit et c est tres rapide.')
st.markdown("- Scentuarize")
st.markdown("- Trois")


st.divider()

st.subheader('Souliman')
message = st.chat_message("assistant")
message.write("Hello Souliman, comment ca va ?")
st.text('This is some text.')

st.divider()

st.subheader('Activite François')
message = st.chat_message("assistant")
message.write("Hello Souliman, comment ca va mon gâte?")

st.text('This is some text.')
