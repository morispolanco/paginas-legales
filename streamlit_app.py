import streamlit as st

# Funciones para cada página
def home_page():
    st.title("Página de Inicio")
    st.write("¡Bienvenido a la Página de Inicio!")

def page_one():
    st.title("Leyes")
    st.write("import streamlit as st
    import requests
    
    def get_api_response(question):
        url = "https://api.afforai.com/api/api_completion"
        payload = {
            "apiKey": "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e",
            "sessionID": "65489d7c9ad727940f2ab26f",
            "history": [
                {
                    "role": "user",
                    "content": question
                }
            ],
            "powerful": True,
            "google": True
        }
        response = requests.post(url, json=payload)
        return response.json()
    
    def main():
        st.title("Preguntas sobre las leyes de Guatemala")
        question = st.text_input("Escribe tu pregunta")
        if st.button("Enviar"):
            response = get_api_response(question)
            st.write(response)
    
    if __name__ == "__main__":
        main()")

def page_two():
    st.title("Página 2")
    st.write("Contenido de la Página 2.")

def page_three():
    st.title("Página 3")
    st.write("Contenido de la Página 3.")

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
