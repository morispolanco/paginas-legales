import streamlit as st
import requests
import json

# Funciones para cada página

def home_page():
    st.title("Página de Inicio")
    st.write("¡Bienvenido a la Página de Inicio!")

def page_one():
    st.title("Página 1: Preguntas sobre las leyes de Guatemala")

    # Código de la API
    def get_api_response(question):
        url = "https://api.afforai.com/api/api_completion"
        payload = {
            "apiKey": "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e",
            "sessionID": "65489d7c9ad727940f2ab26f",
            "history": [{"role": "user", "content": question}],
            "powerful": True,
            "google": True
        }
        response = requests.post(url, json=payload)
        return response.json()

    # Interfaz de usuario
    question = st.text_input("Escribe tu pregunta")
    if st.button("Enviar"):
        response = get_api_response(question)
        st.subheader("Respuesta:")
        st.write(response)

def page_two():
    st.title("Página 2: Jurisprudencia de Guatemala Q&A")

    # Configuración de la API
    API_KEY = "260cee54-6d54-48ba-92e8-bf641b5f4805"
    url = "https://api.respell.ai/v1/run"

    # Interfaz de usuario
    user_question = st.text_input("Ingrese su pregunta:")

    # Función para realizar la solicitud a la API
    def make_api_request(question):
        headers = {
            "authorization": f"Bearer {API_KEY}",
            "accept": "application/json",
            "content-type": "application/json",
        }

        data = {
            "spellId": "XuGwQnVX4hETVI1ZVHKlD",
            "inputs": {"input": question},
        }

        response = requests.post(url, json=data, headers=headers)
        return response.json() if response.status_code == 200 else None

    # Botón para enviar la solicitud a la API
    if st.button("Enviar solicitud"):
        # Verificar si se ha ingresado una pregunta
        if user_question:
            # Realizar la solicitud a la API
            api_response = make_api_request(user_question)

            # Verificar si la respuesta de la API es válida
            if api_response:
                # Mostrar la respuesta en la aplicación
                st.subheader("Respuesta:")
                st.write(api_response)
            else:
                st.warning("No se pudo obtener una respuesta. Inténtelo nuevamente.")
        else:
            st.warning("Ingrese una pregunta antes de enviar la solicitud.")

def page_three():
    st.title('Página 3: Información sobre trámites legales en Guatemala')

    # Función para obtener datos de la API
    def get_tramite_info(text):
        url = 'https://api.respell.ai/v1/run'
        payload = json.dumps({
            "spellId": "MC99TFR1pu8M1GE_uXxo_",
            "inputs": {"input": text}
        })
        headers = {
            'authorization': 'Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805',
            'accept': 'application/json',
            'content-type': 'application/json'
        }
        response = requests.post(url, headers=headers, data=payload)
        return response.json() if response.status_code == 200 else None

    # Interfaz de usuario
    user_input = st.text_input('Ingrese el texto para consultar información sobre trámites:')
    if st.button('Obtener Información'):
        result = get_tramite_info(user_input)
        if result:
            st.subheader('Resultado:')
            st.json(result)
        else:
            st.error('Error al obtener la información, intente nuevamente.')

# Configuración de la aplicación Streamlit

st.sidebar.title("Menú de Navegación")
pages = ["Home", "Página 1", "Página 2", "Página 3"]
selected_page = st.sidebar.selectbox("Selecciona una página", pages)

# Renderizar la página seleccionada

if selected_page == "Home":
    home_page()
elif selected_page == "Página 1":
    page_one()
elif selected_page == "Página 2":
    page_two()
elif selected_page == "Página 3":
    page_three()
