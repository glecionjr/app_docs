import configparser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Conexao():

    def conectar(self):
        config = configparser.ConfigParser()
        config.read('..\config.ini')

        user = config['DATABASE']['user']
        password = config['DATABASE']['password']
        dbname = config['DATABASE']['dbname']
        host = config['DATABASE']['host']
        port = int(config['DATABASE']['port'])

        engine = create_engine(f'postgres://{user}:{password}@{host}:{port}/{dbname}')

        # Conexão ao banco de dados
        return engine

    def criar_sessao(self):
        conexao = self.conectar()

        # Criar uma sessao sem comunicacao. Apenas o objeto
        Session = sessionmaker()

        # A sessão será com o banco de dados do objeto 'conexao'
        Session.configure(bind=conexao)

        session = Session()

        return session
