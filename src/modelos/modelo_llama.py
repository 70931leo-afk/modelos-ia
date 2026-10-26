# install langchain_ollama
from langchain_ollama import ChatOllama

class Modelollama:
    def __init__(self):
        self.modelo = ChatOllama(model="llama3.2:3b", temperature=0.7)

    def generar_respuesta(self, prompt):
        respuesta = self.modelo.invoke(prompt)
        return respuesta.text