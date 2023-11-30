from model.contato_model import *

class BancoDeDados:
    def __init__(self, conexao):
        self.conexao = conexao
        self.criar_tabela()

    def criar_tabela(self):
        with self.conexao.conn.cursor() as cursor:
            query = '''
            CREATE TABLE IF NOT EXISTS contatos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(50),
                sobrenome VARCHAR(50),
                aniversario DATE,
                email VARCHAR(50),
                telefone VARCHAR(20),
                descricao TEXT
            );
            '''
            cursor.execute(query)
        self.conexao.conn.commit()

    def adicionar_contato(self, contato):
        """
        Inserts a new contact into the 'contatos' table.

        Parameters:
            contato (Contact): The contact object to be inserted into the table.

        Returns:
            None
        """
        with self.conexao.conn.cursor() as cursor:
            query = '''
            INSERT INTO contatos (nome, sobrenome, aniversario, email, telefone, descricao)
            VALUES (%s, %s, %s, %s, %s, %s);
            '''
            cursor.execute(query, (contato.nome, contato.sobrenome, contato.aniversario,
                                   contato.email, contato.telefone, contato.descricao))
        self.conexao.conn.commit()

    def obter_contatos(self):
        with self.conexao.conn.cursor() as cursor:
            query = 'SELECT * FROM contatos;'
            cursor.execute(query)
            return cursor.fetchall()

    def atualizar_contato(self, contato):
        with self.conexao.conn.cursor() as cursor:
            query = '''
            UPDATE contatos
            SET nome = %s, sobrenome = %s, aniversario = %s, email = %s, telefone = %s, descricao = %s
            WHERE id = %s;
            '''
            cursor.execute(query, (contato.nome, contato.sobrenome, contato.aniversario,
                                   contato.email, contato.telefone, contato.descricao, contato.id))
        self.conexao.conn.commit()

    def excluir_contato(self, contato_id):
        with self.conexao.conn.cursor() as cursor:
            query = 'DELETE FROM contatos WHERE id = %s;'
            cursor.execute(query, (contato_id,))
        self.conexao.conn.commit()

    def obter_contato_por_id(self, contato_id):
        with self.conexao.conn.cursor() as cursor:
            query = 'SELECT * FROM contatos WHERE id = %s;'
            cursor.execute(query, (contato_id,))
            contato_data = cursor.fetchone()

        if contato_data:
            # Se houver dados, criar um objeto Contato
            contato = Contato(*contato_data)
            return contato
        else:
            return None
