from src.modelos.modelo_conectar import Prompt_Conexion
from src.modelos.modelo_roles import Prompt_Roles
from src.modelos.prompt_02 import Prompt_02
from src.modelos.prompt_01 import Prompt
from src.modelos.modelo_llama import Modelollama
from src.modelos.modelo_google import ModeloGoople
from src.modelos.modelo_groq import ModeloGroq
from src.modelos.modelo_local import ModeloLocal
import os 
from rich.console import Console
from rich.markdown import Markdown

class Menu_Principal():
    def __init__(self):
        self.console = Console()
        self.opcion = 0

    @staticmethod
    def limpiar_pantalla():
        # Limpiar la pantalla según el sistema operativo
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def pausar():
        input("Presione Enter para continuar...")

    def mostrar_menu(self):
        print("=== Menú Principal ===")
        print("1. Modelo Google API KEY")
        print("2. Modelo Groq API KEY")
        print("3. Modelo Local")
        print("4. Modelo llama")
        print("5. Prompt 01_basico")
        print("6. Prompt 02_template")
        print("7. Prompt 03_modelos_roles")
        print("8. Prompt conexion")
        print("0. Salir")

    def ejecutar_opcion(self):
        while True:
                self.limpiar_pantalla()
                self.mostrar_menu()
                self.opcion = input("Seleccione una opción: ")

                if self.opcion == "1":
                    modelo_google = ModeloGoople()
                    prompt = input("Ingrese el prompt para el modelo Google: ")
                    respuesta = modelo_google.generar_respuesta(prompt)
                    print(f"Respuesta del modelo Google: ")
                    self.console.print(Markdown(respuesta))     
                    
                    # Lógica para la Opción 1
                elif self.opcion == "2":
                    modelo_groq = ModeloGroq()
                    prompt = input("Ingrese el prompt para el modelo Groq: ")
                    respuesta = modelo_groq.generar_respuesta(prompt)       
                    print(f"Respuesta del modelo Groq: ")
                    self.console.print(Markdown(respuesta)) 
                    
                elif self.opcion == "3":
                    modelo_local = ModeloLocal()
                    prompt = input("Ingrese el prompt para el modelo Local: ")  
                    respuesta = modelo_local.generar_respuesta(prompt)
                    print(f"Respuesta del modelo Local: ")
                    self.console.print(Markdown(respuesta))

                elif self.opcion == "4":
                    modelo_llama = Modelollama()
                    prompt = input("Ingrese el prompt para el modelo Llama: ")  
                    respuesta = modelo_llama.generar_respuesta(prompt)
                    print(f"Respuesta del modelo Llama: ")
                    self.console.print(Markdown(respuesta)) 

                elif self.opcion == "5":
                    prompt_model = Prompt()
                    prompt = input("Ingrese el prompt para el modelo Llama: ")  
                    respuesta = prompt_model.generar_respuesta(prompt)
                    print(f"Respuesta del prompt 01: ")
                    self.console.print(Markdown(respuesta))

                elif self.opcion == "6":    
                    prompt_model_02 = Prompt_02()
                    respuesta = prompt_model_02.generar_respuesta()
                    print(f"Respuesta del prompt 02: ")
                    self.console.print(Markdown(respuesta))

                elif self.opcion == "7":    
                    prompt_roles = Prompt_Roles()
                    respuesta = prompt_roles.generar_respuesta()
                    print(f"Respuesta del prompt roles: ")
                    self.console.print(Markdown(respuesta))
                elif self.opcion == "8":    
                    prompt_conexion = Prompt_Conexion()
                    respuesta = prompt_conexion.generar_respuesta()
                    print(f"Respuesta del prompt conexion: ")
                    self.console.print(Markdown(respuesta))

                elif self.opcion == "0":
                    print("Saliendo del menú principal...")
                    break
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")
                self.pausar()