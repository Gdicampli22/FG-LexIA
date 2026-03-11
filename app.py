import streamlit as st
from modules import analisis_casos, generacion_docs, chat_legal

# Configuración inicial de la página
st.set_page_config(
    page_title="LexIA - Dra. Flavia Guevara",
    page_icon="⚖️",
    layout="wide"
)

# Título y bienvenida
st.title("⚖️ LexIA - Estudio Jurídico Dra. Flavia Guevara")
st.subheader("Asistente Legal Inteligente y Estratégico")

# Barra lateral para navegación
st.sidebar.title("Menú de Herramientas")
# ... (el resto del archivo queda igual)
opcion = st.sidebar.radio(
    "Selecciona una función:",
    ("🔍 Análisis de Casos y Jurisprudencia", 
     "📄 Generación de Documentos", 
     "💬 Chat Legal Especializado")
)

st.sidebar.markdown("---")
st.sidebar.info("LexIA v1.0 (MVP) - Optimizando el flujo de trabajo jurídico.")

# Enrutamiento a los módulos
if opcion == "🔍 Análisis de Casos y Jurisprudencia":
    analisis_casos.mostrar_interfaz()
elif opcion == "📄 Generación de Documentos":
    generacion_docs.mostrar_interfaz()
elif opcion == "💬 Chat Legal Especializado":
    chat_legal.mostrar_interfaz()