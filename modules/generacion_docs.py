import streamlit as st
from utils.llm_api import generar_respuesta_legal

def mostrar_interfaz():
    st.header("📄 Generador de Escritos Judiciales y Extrajudiciales")
    st.write("Completa los datos clave y LexIA redactará un borrador profesional adaptado a los tribunales de Córdoba y la legislación nacional.")
    
    # 1. Configuración del documento
    col1, col2 = st.columns(2)
    with col1:
        tipo_documento = st.selectbox(
            "Tipo de Escrito:",
            [
                "Carta Documento (Laboral - Intimación LCT)", 
                "Demanda (Daños y Perjuicios)", 
                "Contestación de Demanda", 
                "Convenio de Divorcio (Presentación Conjunta)",
                "Recurso de Apelación"
            ]
        )
    with col2:
        fuero = st.selectbox(
            "Fuero / Jurisdicción:", 
            ["Provincial (Córdoba Capital)", "Provincial (Interior de Córdoba)", "Federal (Córdoba)"]
        )
    
    st.markdown("---")
    
    # 2. Datos de las partes
    st.subheader("Datos de las Partes")
    col3, col4 = st.columns(2)
    with col3:
        parte_actora = st.text_input("Parte Actora / Remitente (Nombre, DNI, Domicilio):", placeholder="Juan Pérez, DNI 12.345.678...")
    with col4:
        parte_demandada = st.text_input("Parte Demandada / Destinatario (Nombre, CUIT, Domicilio):", placeholder="Empresa S.A., CUIT 30-...")

    # 3. El corazón del asunto
    hechos = st.text_area(
        "Descripción de los Hechos (Materia prima para la IA):", 
        height=150,
        help="Cuanto más detallados sean los hechos, fechas y montos, mejor será el documento generado."
    )

    # 4. Automatización
    if st.button("🚀 Generar Documento Legal", type="primary"):
        if not hechos or not parte_actora or not parte_demandada:
            st.error("⚠️ Faltan datos. Por favor completa las partes y los hechos.")
        else:
            with st.spinner("LexIA está redactando... Aplicando Código Procesal y jurisprudencia..."):
                
                # EL PROMPT: Instrucciones hiper-específicas para el modelo
                prompt_redaccion = f"""
                Actúa como un abogado litigante experto matriculado en la provincia de Córdoba, Argentina.
                Tu tarea es redactar el siguiente documento legal: {tipo_documento}.
                Jurisdicción y Fuero: {fuero}.
                
                DATOS DE LAS PARTES:
                - Parte Actora / Remitente: {parte_actora}
                - Parte Demandada / Destinatario: {parte_demandada}
                
                HECHOS:
                {hechos}
                
                INSTRUCCIONES DE REDACCIÓN:
                1. Estructura: Utiliza la estructura formal requerida por los tribunales de Córdoba (o formato oficial de Correo Argentino si es Carta Documento).
                2. Normativa: Cita los artículos pertinentes de la legislación de fondo (ej. LCT, CCyCN) y de forma (CPCC de Córdoba).
                3. Tono: Jurídico, imperativo, formal y preciso.
                4. Cierre: Incluye la fórmula de cierre correspondiente (ej. "Proveer de conformidad, SERÁ JUSTICIA" o "Queda usted debidamente notificado").
                5. Importante: No dejes campos en blanco [como este], inventa datos coherentes de relleno si falta algún detalle menor, o usa '...' para que el profesional lo complete.
                """
                
                # Llamada a nuestro cerebro central con temperatura baja para evitar alucinaciones
                documento_generado = generar_respuesta_legal(prompt_redaccion, temperatura=0.1)
                
                st.success("✅ Documento generado exitosamente.")
                
                # Mostrar el resultado en un área de texto para que se pueda editar ahí mismo
                st.text_area("Borrador Generado (Puedes editarlo aquí):", value=documento_generado, height=400)
                
                # Opción de descarga
                st.download_button(
                    label="⬇️ Descargar Borrador (.txt)", 
                    data=documento_generado, 
                    file_name=f"borrador_{tipo_documento.replace(' ', '_')}.txt"
                )