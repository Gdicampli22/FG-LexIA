import streamlit as st
from utils.llm_api import generar_respuesta_legal

def mostrar_interfaz():
    st.header("🔍 Análisis Automático de Casos")
    st.write("Ingresa los hechos del cliente. LexIA analizará la viabilidad, normativa aplicable (Córdoba/Nación) y propondrá una estrategia.")
    
    # 1. Interfaz de entrada de datos
    area_derecho = st.selectbox(
        "Rama del Derecho:",
        ["Derecho Laboral", "Derecho Civil y Comercial", "Derecho de Familia", "Sucesiones"]
    )
    
    hechos = st.text_area(
        "Relato de los hechos (lo que cuenta el cliente):",
        height=200,
        placeholder="Ej: El cliente trabajó 5 años en negro como cajero. Lo despidieron verbalmente ayer..."
    )
    
    # 2. Botón de acción para disparar la automatización
    if st.button("🧠 Analizar Caso con FG-LexIA", type="primary"):
        if not hechos.strip():
            st.warning("Por favor, ingresa los hechos del caso para poder analizarlo.")
        else:
            with st.spinner("LexIA está analizando la jurisprudencia y normativa aplicable..."):
                
                # 3. El Prompt Estructurado: Aquí está el verdadero motor de la automatización
                prompt_analisis = f"""
                Actúa como el abogado socio y estratega principal del estudio de la Dra. Flavia Guevara en Córdoba.
                Analiza los siguientes hechos del cliente para la rama: {area_derecho}.
                
                HECHOS:
                "{hechos}"
                
                Genera un informe estratégico ultra profesional con la siguiente estructura:
                
                1. DIAGNÓSTICO JURÍDICO: Viabilidad del caso y encuadre legal (leyes nacionales y código de Córdoba).
                2. RIESGOS Y PRUEBAS: Qué puntos débiles hay y qué pruebas urgentes se deben recolectar.
                3. PLAN DE ACCIÓN PASO A PASO: Cuál es la estrategia a seguir para ganar o resolver el conflicto (ej. mediación, cautelar, demanda).
                4. 📋 DOCUMENTOS A GENERAR (HOJA DE RUTA): Enumera en formato de lista (bullet points) exactamente qué escritos, oficios o telegramas debe redactar la Dra. Guevara a continuación para ejecutar el paso 1 del plan de acción.
                
                Tu objetivo es facilitarle el trabajo procesal a la Dra. Guevara, siendo claro, directo y muy resolutivo.
                """
                
                # 4. Llamada a nuestra API centralizada
                resultado_analisis = generar_respuesta_legal(prompt_analisis, temperatura=0.2)
                
                # 5. Mostrar resultados
                st.success("Análisis completado.")
                st.markdown("### 📑 Informe de Estrategia Legal")
                st.markdown(resultado_analisis)
                
                # Opción para que tu cuñada pueda guardar el análisis
                st.download_button(
                    label="⬇️ Descargar Análisis (.txt)",
                    data=resultado_analisis,
                    file_name="analisis_caso_lexia.txt"
                )