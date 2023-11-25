import streamlit as st

# Funciones para cada página
def home_page():
    st.title("Página de Inicio")
    st.write("¡Bienvenido a la Página de Inicio!")

def page_one():
    st.title("Página 1")
    st.write("Contenido de la Página 1.")

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
