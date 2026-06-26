# MDR-Gemini-Bot
Bot experto en Regulatory Affairs MDR 2017/745 UE con Gemini 1.5 Flash. 

Te guía paso a paso hasta tener la clasificación + borrador de Documentación Técnica Anexo II/III. Solo necesitas el nombre del dispositivo.

## ¿Qué hace este bot?
1.  **Te pregunta solo lo que falta**: 1 o 2 preguntas a la vez, sin jerga regulatoria.
2.  **Clasifica automático**: Te dice Clase I, IIa, IIb o III + Regla exacta del Anexo VIII + por qué.
3.  **Te da el borrador del Anexo II**: Descripción, uso previsto, principio de funcionamiento, etc. en viñetas.

*Aviso: Es un borrador informativo. Hay que validarlo siempre con un Notified Body.*

## Instalación
1.  `pip install -r requirements.txt`
2.  Copia `.env.example` a `.env` y mete tu `GEMINI_API_KEY` de https://aistudio.google.com
3.  `python app.py`

## Cómo usarlo
Solo escribe el dispositivo. El bot hace el resto.

**Ejemplo de conversación:**
## Ejemplo de conversación

**Tú:** `Hola, quiero clasificar un nuevo software médico.`

**Bot:** `Perfecto, te ayudaré con la clasificación bajo MDR 2017/745. 
     ¿Cuál es el uso previsto exacto de este software? 
     ¿Toma decisiones diagnósticas o terapéuticas, o solo monitoriza variables?`

**Tú:** `Monitoriza SpO2 con un pulsioxímetro de dedo`

**Bot:** `¿Es invasivo o solo toca la piel? ¿Cuánto dura cada medición?`

*... [el bot pregunta hasta tener todo] ...*

**Bot:** 
Clasificación: Clase IIa
Regla MDR: Regla 10 
Razonamiento: Dispositivo activo de diagnóstico para medir SpO2. No monitoriza funciones vitales críticas en tiempo real.Borrador Anexo II (Sección 1): 
- Nombre comercial/genérico: Pulsioxímetro de dedo
- Uso previsto: Medición no invasiva de SpO2 y pulso
- Principio de funcionamiento: LED + fotodiodo transcutáneo-
- Clasificación propuesta: Clase IIa (Regla 10)

*Disclaimer: Borrador informativo y preliminar. Validar con un Notified Body (Organismo Notificado).*


## Datos que el bot te va a preguntar
Para clasificar bien según MDR, te preguntará sobre:
- **Uso previsto y principio**: ¿Para qué sirve? ¿Necesita pilas/corriente?
- **Invasividad**: ¿Piel, orificio, quirúrgico/implantable?
- **Duración**: ¿<60min, <30 días, >30 días?
- **Contacto**: ¿Piel, mucosa, sangre, SNC?
- **Función especial**: ¿Medicamento? ¿Software?

## Licencia
MIT License. Ver archivo `LICENSE`. 

**Disclaimer legal**: Esta herramienta no sustituye la evaluación de conformidad MDR por un Organismo Notificado. Uso bajo responsabilidad del fabricante.
