import streamlit as st
from PIL import Image

st.balloons()

image = Image.open('GuillaumeSourireMagique.jpg')
st.image(image, caption='Un BG se cache dans cette image. Pouvez-vous le retrouver ?')

st.title('To-do list pour une reprise en douceur')

message = st.chat_message("assistant")
message.write("Note importante : A compter de votre retour, tous vos projets doivent être dans Orchestra. Pensez donc à bien mettre à jour tous vos projets dans le logiciel. Le lien est le suivant https://mane.orchestra-ppm.cloud/cpms/")
message.write("A compte du 28 aout, nous ferons des reunions de suivi de projets de 30 mn par personne pour strucuter les (nombreux) projets que nous avons.")


st.divider()


st.subheader('Guillaume')

st.markdown(st.subheader("- LLM "))
st.write('Comme tu le vois, on a découvert streamlit. A mon avis c est vraiment pas mal pour des petits formats d applis et je vois parfaitement ce genre de format pour le projet LLM. Tu peux aussi deployer des applis avec HuggingFace en streamlit et c est tres rapide.')

st.markdown(st.subheader("- Scentuarize"))
st.write('Julien partira un mois plus tôt pour faire une année supplémentaire.')

st.markdown("- Trois")


st.divider()

st.subheader('Souliman')

st.text('This is some text.')

st.divider()

st.subheader('Activite François')
message = st.chat_message("assistant")
message.write("Hello Souliman, comment ca va mon gâte?")

st.text('This is some text.')

col1, col2, col3 = st.columns(3)
col1.write('Column 1')
col2.write('Column 2')
col3.write('Column3')


