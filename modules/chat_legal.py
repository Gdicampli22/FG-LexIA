import streamlit as st
from utils.llm_api import generar_respuesta_legal

def mostrar_interfaz():
    st.header("💬 Chat Legal Especializado")
    st.write("Consulta a LexIA como si fuera un colega de guardia. Ideal para dudas rápidas sobre plazos procesales, jurisprudencia o doctrina.")

    # 1. Memoria de la sesión: Esto permite que el chat recuerde la conversación
    # mientras el usuario no recargue la página.
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = [
            {"rol": "assistant", "contenido": "Hola, colega. ¿En qué puedo ayudarte hoy con la normativa o jurisprudencia de Córdoba/Nación?"}
        ]

    # 2. Dibujar el historial de mensajes en la pantalla
    for mensaje in st.session_state.mensajes:
        with st.chat_message(mensaje["rol"]):
            st.markdown(mensaje["contenido"])

    # 3. Caja de texto para que el usuario escriba su consulta
    pregunta = st.chat_input("Ej: ¿Cuál es el plazo para contestar una demanda abreviada en Córdoba?")

    if pregunta:
        # Mostrar la pregunta del usuario en la interfaz
        with st.chat_message("user"):
            st.markdown(pregunta)
        
        # Guardar la pregunta en la memoria temporal
        st.session_state.mensajes.append({"rol": "user", "contenido": pregunta})

        # 4. Generar la respuesta automatizada
        with st.chat_message("assistant"):
            with st.spinner("Buscando en códigos y jurisprudencia..."):
                
                # Armamos un prompt específico para modo "charla rápida"
                # Le damos un poco más de temperatura (0.3) para que sea conversacional pero preciso.
                prompt_chat = f"""
                Un abogado te hace la siguiente consulta rápida:
                "{pregunta}"
                
                Responde de manera directa, concisa y profesional. Cita los artículos específicos de las leyes nacionales (LCT, CCyCN) o del Código Procesal Civil y Comercial (CPCC) de Córdoba según corresponda. 
                Actúa como un colega experimentado respondiendo una duda en los pasillos de Tribunales.
                """
                
                respuesta = generar_respuesta_legal(prompt_chat, temperatura=0.3)
                st.markdown(respuesta)
        
        # Guardar la respuesta de la IA en la memoria
        st.session_state.mensajes.append({"rol": "assistant", "contenido": respuesta})

    # 5. Botón para reiniciar la charla
    st.markdown("---")
    if len(st.session_state.mensajes) > 1:
        if st.button("🗑️ Limpiar Conversación"):
            st.session_state.mensajes = [
                {"rol": "assistant", "contenido": "Historial borrado. ¿Qué nueva consulta tenés?"}
            ]
            st.rerun() # Recarga la interfaz para limpiar la pantalla