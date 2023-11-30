import tkinter as tk
from model.conexao_banco import ConexaoBanco
from model.banco_de_dados_model import BancoDeDados
from model.contato_model import Contato
from controller.contato_controller import ContatoController
from view.interface_grafica_view import InterfaceGrafica

if __name__ == "__main__":
    root = tk.Tk()

    controller = ContatoController() 
    app = InterfaceGrafica(root, controller)

    root.mainloop()
