import psycopg2

class ConexaoBanco:
    def __init__(self, dbname, user, password, host):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
        )

    def fechar_conexao(self):
        self.conn.close()
