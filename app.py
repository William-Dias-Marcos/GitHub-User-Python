import requests
import streamlit as st
from streamlit_card import card

st.set_page_config(
    page_title="GitHub",
    page_icon="https://github.com/fluidicon.png", 
    layout="centered"
)
BASE_URL = 'https://api.github.com'

def selectUser(username):
    url = f'{BASE_URL}/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def frontend():

    st.title('Buscar usuário do GitHub')

    username = st.text_input('Digite o nome do usuário...')

    if st.button('Buscar'):
        infoUser = selectUser(username) 
        if infoUser is not None: 

            card(
                title=infoUser['name'], 
                text=infoUser['bio'],
                url=infoUser['html_url'], 
                image=infoUser['avatar_url'],
                styles={
                    "div": {
                        "padding": "1px",
                    },
                    "card": {
                        "width": "100vw",
                        "height": "400px",
                        "max-width": "400px",
                        "border-radius": "60px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                    },
                    "filter": {
                    "background-color": "rgba(0, 0, 0, 0)",
                    "position": "static"
                    },
                    "text": {
                        "padding-bottom": "10px",
                    }
                }
                )
            
        else:
            st.error('Usuário não encontrado!')


frontend()