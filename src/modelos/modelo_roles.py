from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

class Prompt_Roles:
    def __init__(self):
        self.modelo = ChatOllama(model="qwen2.5:3b", temperature=0.1)
    def generar_respuesta(self):
        plantilla = ChatPromptTemplate.from_messages([
            ("system",
             """
             
             Eres un profesor universitario de programacion.

             Instrucciones:

             - Responde siempre en español.
             - Utiliza lenguaje sencillo.
             - Explica los conceptos paso a paso.
             - Incluye un ejemplo en python.
             - No utilices tecnisismos innecesarios.
             """
             ) ,
             ("human",
              "Explicame el siguientete tema : {tema}")
        ]) 
        mensaje = plantilla.invoke({"tema": "estructuras condicionales"})
        respuesta = self.modelo.invoke(mensaje)
        return respuesta.text   