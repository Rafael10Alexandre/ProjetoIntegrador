from model.conexao_banco import ConexaoBanco
from model.banco_de_dados_model import BancoDeDados
from model.contato_model import Contato

class ContatoController:
    def __init__(self):
        # Inicializar a conexão no controlador
        self.conexao = ConexaoBanco(dbname='postgres'
                                    ,user='postgres'
                                    ,password='abc12345'
                                    ,host='localhost')

        # Inicializar o modelo com a conexão
        self.model = BancoDeDados(self.conexao)

    def adicionar_contato(self, nome, sobrenome, aniversario, email, telefone, descricao):
        novo_contato = Contato(nome=nome, sobrenome=sobrenome, aniversario=aniversario,
                               email=email, telefone=telefone, descricao=descricao, id=None)
        self.model.adicionar_contato(novo_contato)

    def atualizar_contato(self, contato_id, nome=None, sobrenome=None, aniversario=None, email=None, telefone=None, descricao=None):
        # Obter os dados do contato atual
        contato_atual = self.obter_contato_por_id(contato_id)

        # Verificar se o contato existe
        if contato_atual:
            # Atualizar apenas os campos fornecidos, mantendo os existentes
            if nome is not None:
                contato_atual.nome = nome
            if sobrenome is not None:
                contato_atual.sobrenome = sobrenome
            if aniversario is not None:
                contato_atual.aniversario = aniversario
            if email is not None:
                contato_atual.email = email
            if telefone is not None:
                contato_atual.telefone = telefone
            if descricao is not None:
                contato_atual.descricao = descricao

            # Atualizar o contato no banco de dados
            self.model.atualizar_contato(contato_atual)
        else:
            print("Contato não encontrado.")

    def excluir_contato(self, contato_id):
        self.model.excluir_contato(contato_id)

    def obter_contatos(self):
        return self.model.obter_contatos()

    def obter_contato_por_id(self, contato_id):
        return self.model.obter_contato_por_id(contato_id)
