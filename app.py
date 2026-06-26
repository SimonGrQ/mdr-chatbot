import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Cargamos tu system_instruction de 1 línea
with open("prompts/system_mdr.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read().strip()

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", # Barato y rápido. Usa "gemini-1.5-pro" si quieres más precisión
    system_instruction=SYSTEM_PROMPT,
    generation_config={"temperature": 0.1} # Bajo para que no invente reglas MDR
)

chat = model.start_chat(history=[])

print("MDR Bot listo. Escribe solo el nombre del dispositivo. Ctrl+C para salir.")
while True:
    user_input = input("\nTú: ")
    response = chat.send_message(user_input)
    print(f"\nBot: {response.text}")
