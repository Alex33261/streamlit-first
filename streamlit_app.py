import streamlit as st

#st.image('streamlit-first/GuillaumeSourireMagique.png')
st.title('To do list pour une reprise en douceur')

st.subheader('Guillaume')
st.caption('Balloons. Hundreds of them...')
message = st.chat_message("assistant")
message.write("Hello Guillaume, alors ces vacances ? Pas trop chaud ? Voilà le topo pour une reprise en douceur...")

st.markdown(st.subheader("- Orchestra "))

st.markdown("- LLM ")
st.write('Comme tu le vois, on a découvert streamlit. A mon avis c est vraiment pas mal pour des petits formats d applis et je vois parfaitement ce genre de format pour le projet LLM. Tu peux aussi deployer des applis avec HuggingFace en streamlit et c est tres rapide.')

st.markdown(st.subheader("- Scentuarize"))
st.write('Julien partira un mois plus tôt pour faire une année supplémentaire.')

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

col1, col2 = st.columns(2)
col1.write('Column 1')
col2.write('Column 2')


