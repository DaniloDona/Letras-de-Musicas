import requests
import streamlit as st

def buscar_letra(banda, musica):
    url = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    resposta= requests.get(url)
    letra= resposta.json()["lyrics"] if resposta.status_code == 200 else ""
    return letra


st.image("https://i.imgur.com/SmktDIH.png")
st.title("LETRAS DE MÚSICAS")

banda= st.text_input("Digite o Nome da Banda: ", key ="banda")
musica= st.text_input("Digite o Nome da Musica: ", key= "musica")
pesquisar= st.button("Pesquisar")

if pesquisar:
    letra= buscar_letra(banda, musica)
    if letra:
        st.success("Sua Música foi Encontrada!")
        st.text(letra)
    else:
        st.error("Não foi possivel achar esta música ")