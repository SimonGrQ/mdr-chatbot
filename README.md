# mdr-chatbot
Bot MDR con Gemini. Le das el nombre de un dispositivo médico y te genera la clasificación + documentación técnica MDR 2017/745 preguntándote solo lo necesario.
# MDR-Gemini-Bot
Bot que genera doc técnica MDR 2017/745 preguntando solo lo necesario.

## Instalar
1. `pip install -r requirements.txt`
2. Copia `.env.example` a `.env` y mete tu `GEMINI_API_KEY`, puedes conseguir la API key gratis en https://aistudio.google.com/app/apikey
3. `python app.py`

## Uso para sanitarios
Escribe: `Pulsioxímetro de dedo` 
El bot te pregunta 3-4 cosas y te suelta la Clasificación + Anexo II completo.

**Aviso**: Borrador informativo. Validar siempre con Notified Body. No es un dispositivo médico.
