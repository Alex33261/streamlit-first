import streamlit as st
from PIL import Image

st.balloons()

image = Image.open('GuillaumeSourireMagique.jpg')
st.image(image, caption='Un BG se cache dans cette image. Pouvez-vous le retrouver ?')

st.title('C est la reprise !')

message = st.chat_message("assistant")
message.write("Note importante : A compter de votre retour, tous vos projets doivent être dans Orchestra. Pensez donc à bien mettre à jour tous vos projets dans le logiciel. Le lien est le suivant https://mane.orchestra-ppm.cloud/cpms/")
message.write("A compte du 28 aout, nous ferons des reunions de suivi de projets de 30 mn par personne pour strucuter les (nombreux) projets que nous avons.")
st.divider()

message = st.chat_message("user")
message.write("Guillaume")

st.markdown("- LLM ")
st.write('Comme tu le vois, on a découvert streamlit. A mon avis c est vraiment pas mal pour des petits formats d applis et je vois parfaitement ce genre de format pour le projet LLM. Tu peux aussi deployer des applis avec HuggingFace en streamlit et c est tres rapide.')
st.write('Tu trouveras beaucoup d infos très intéressantes pour le projet Arômes que nous allons construire à la rentrée, notamment la réunion du 22 aout. Ce sont des infos techniques qui pourraient t aider à te projeter dans quelque chose de concret')
st.write('https://langchain-examples.streamlit.app/')
st.write('Creuse autour de de ce lien et de tous les autres liens que tu pourras trouver autour de LLM. Pense deja aussi a quelques exemples tres concrets de ce a quoi pourrait ressembler le ManeInsightGPT. Nous soumettrons ces exemples lors de la reunion du 22.')

st.markdown("- Scentuarize")
st.write('Julien partira un mois plus tôt pour faire une année supplémentaire sur un troisieme cycle. Il partira debut septembre. Nous avons eu une reunion avec David et une autre avec Julien et il a reussi a coller les deux dashboards')
st.write('Il a reussi a pas mal avancer et a gagner en temps dans le traitements des donnees. Tu peux te rapprocher de lui pour reprendre le fil.')

st.markdown("- Gestion de stagiaires : Mathilde et Chloe")
st.write('Mathilde sera parti quand tu seras de retour. Son code est consigne dans une dossier qui s appelle Sources et auquel elle nous a donne acces. Tu trouveras dans ta boite mail le lien à son drive. Voila ce que j aimerais que tu fasses')
st.write('1 - Prendre son dossier dans le cloud et le mettre au propre dans Gitlab - le repo existe deja')
st.write('2 - Te rapprocher de Fanny pour promouvoir l outil dans son equipe car Mathilde n a pas eu beaucoup de temps pour le faire.')

st.write('Pour Chloe, on s est vu ensemble ce matin du 4 aout et les choses sont claires pour elle. Elle va se pencher sur une appli ou il y a du click event. Regarde avec elle si elle a des galeres de maniere generale.

st.divider()

message = st.chat_message("user")
message.write("Souliman")

st.markdown("- TechniScent")
st.write('L objectif est d integrer le travail de Lenaig dans un nouvel onglet de TechniScent avant la reunion du 8 septembre. J aimerais que tu puisse suivre son travail. Voila ce qu elle a à faire')
st.write('1 - Mettre en place une information sur l ecart-type de la prediction fait à partir des comparaisons reel/predit de son jeu de test')
st.write('2 - Obtenir un jeu de validation (une centaine de formules de Yann Lenne - equipe de Laurent Bacoux) et faire tourner sur l appli directement. En sortir une valeur pratique de l ecart type')
st.write('3 - Ameliorer l UI de maniere simple')
st.write('De maniere generale, laisse la progresse à son rythme et integre son travail à te dernière version de TechniScent quand elle a fini. Pense aussi à demander à François le nouveau logo et une petite palette de couleur pour mettre le nouvel UI de TechniScent en place.')

st.markdown("- Projet Arômes")
st.write('https://langchain-text-summarization.streamlit.app/')
st.write('https://nlu.johnsnowlabs.com/')
st.write('https://github.com/JohnSnowLabs/nlu')

st.divider()

message = st.chat_message("user")
message.write("François")

st.markdown("- TechniScent")
st.write("Texte ici")



