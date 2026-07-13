# MDR-Gemini-Bot
Expert bot in EU MDR 2017/745 Regulatory Affairs powered by Gemini 1.5 Flash. 

It guides you step-by-step until you get the classification + draft of the Annex II/III Technical Documentation. All you need is the name of the device.

## What does this bot do?
1. **Asks only what is missing**: 1 or 2 questions at a time, without regulatory jargon.
2. **Automatic classification**: Tells you the Class (I, IIa, IIb or III) + exact Rule of Annex VIII + the rationale.
3. **Provides the Annex II draft**: Description, intended purpose, principle of operation, etc. in bullet points.

*Notice: This is an informative draft. It must always be validated with a Notified Body.*

## Installation
1. `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and insert your `GEMINI_API_KEY` from https://aistudio.google.com
3. `python app.py`

## How to use it
Just type the name of the device. The bot does the rest.

## Conversation Example

**You:** `Hi, I want to classify a new medical software.`

**Bot:** `Perfect, I will help you with the classification under MDR 2017/745. 
     What is the exact intended purpose of this software? 
     Does it make diagnostic or therapeutic decisions, or does it only monitor variables?`

**You:** `It monitors SpO2 with a fingertip pulse oximeter.`

**Bot:** `Is it invasive or does it only touch the skin? How long does each measurement last?`

*... [the bot asks questions until it has everything it needs] ...*

**Bot:** 
Classification: Class IIa
MDR Rule: Rule 10 
Rationale: Active diagnostic device for measuring SpO2. It does not monitor critical vital functions in real time.

Annex II Draft (Section 1): 
- Commercial/generic name: Fingertip pulse oximeter
- Intended purpose: Non-invasive measurement of SpO2 and pulse
- Principle of operation: LED + transcutaneous photodiode
- Proposed classification: Class IIa (Rule 10)

*Disclaimer: Informative and preliminary draft. Validate with a Notified Body.*


## Data the bot will ask you for
To properly classify the device according to the MDR, it will ask you about:
- **Intended purpose and principle**: What is it for? Does it require batteries/mains power?
- **Invasiveness**: Skin, orifice, surgically invasive/implantable?
- **Duration**: <60 min, <30 days, >30 days?
- **Contact**: Skin, mucosa, blood, CNS?
- **Special function**: Medicinal product? Software?

## Licence
MIT Licence. See `LICENSE` file. 

**Legal Disclaimer**: This tool does not replace the MDR conformity assessment by a Notified Body. Use at the manufacturer's own responsibility.


------------------------------------------------------------------------------------------------------------------------------------------------

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
