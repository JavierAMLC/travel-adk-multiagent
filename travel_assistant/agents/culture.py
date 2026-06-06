from google.adk.agents import Agent

from travel_assistant.tools.culture_tools import get_local_culture_data

local_culture_agent = Agent(
    name="local_culture_agent",
    model="gemini-2.5-flash",
    description="Recomienda platos típicos, costumbres y frases útiles del lugar de destino.",
    instruction="""
Eres un experto en cultura regional y gastronomía local. 
Tu tarea es proporcionar platos típicos, costumbres y frases útiles
usando la herramienta get_local_culture_data.
Rules:
1. Responde siempre de manera entusiasta sobre la cultura.
2. Destaca la importancia de respetar las costumbres locales.
3. Muestra las frases típicas de forma clara para que el estudiante pueda aprenderlas rápidamente.
""",
    tools=[get_local_culture_data],
)