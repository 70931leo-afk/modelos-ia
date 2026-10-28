from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class Prompt_Conexion:
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
        cadena = plantilla | self.modelo | StrOutputParser()

        mensaje = cadena.invoke({"tema": "estructuras de datos"})
        respuesta = self.modelo.invoke(mensaje)
        return respuesta.text   