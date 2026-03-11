import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

# Configuración de la API de Google
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("⚠️ Error crítico: No se encontró GEMINI_API_KEY en el archivo .env")
else:
    genai.configure(api_key=api_key)

def generar_respuesta_legal(prompt_usuario: str, temperatura: float = 0.1) -> str:
    """
    Se comunica con Gemini aplicando reglas estrictas de derecho argentino.
    """
    
    # El System Prompt define las reglas de juego
    system_instruction = """
    Eres LexIA, el Asistente Legal Inteligente exclusivo del Estudio Jurídico de la Dra. Flavia Guevara, en la Provincia de Córdoba, Argentina.
    
    TUS REGLAS ESTRICTAS:
    1. Base Normativa: Fundamenta en el CCyCN, LCT y el Código Procesal Civil y Comercial de Córdoba.
    2. Proactividad: Eres extremadamente servicial. Siempre debes proponer cómo seguir con la causa y qué documentos exactos redactar.
    3. Tono: Formal, técnico, objetivo y propio de un abogado litigante de primer nivel.
    4. Advertencia: Tus borradores son propuestas estratégicas para que la Dra. Guevara los revise y firme.
    """

    try:
        # Usamos el modelo Gemini 1.5 Flash (súper rápido e ideal para procesar texto)
        # o Gemini 1.5 Pro si necesitas razonamiento jurídico hiper complejo.
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=system_instruction,
            generation_config=genai.types.GenerationConfig(
                temperature=temperatura,
                max_output_tokens=4000,
            )
        )
        
        # Generamos la respuesta
        respuesta = model.generate_content(prompt_usuario)
        return respuesta.text
        
    except Exception as e:
        return f"⚠️ Ocurrió un error en la conexión con Gemini: {str(e)}"

# --- Bloque de prueba local ---
if __name__ == "__main__":
    print("Probando conexión con Gemini para LexIA...")
    prueba_prompt = "Redacta un breve párrafo intimando al pago de indemnización por despido incausado según la LCT argentina."
    resultado = generar_respuesta_legal(prueba_prompt)
    print("\nResultado de la prueba:\n")
    print(resultado)