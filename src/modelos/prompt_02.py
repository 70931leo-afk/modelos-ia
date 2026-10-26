from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate 



class Prompt_02:
    def __init__(self):
        self.modelo = ChatOllama(model="qwen2.5:3b", temperature=0.1)
    
    def generar_respuesta(self):
        prompt_template = PromptTemplate.from_template("Explica el concepto de {tema}"
                                                       "para un estudiante de nivel {nivel}."
                                                       "Proporciona ejemplos y analogías para facilitar la comprensión."
                                                       )
        prompt = prompt_template.format(tema="inteligencia artificial",  nivel="universitario")
        print(f"Prompt generado: {prompt}")
        respuesta = self.modelo.invoke(prompt)
        return respuesta.text