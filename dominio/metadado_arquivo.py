class Arquivo():

    def __init__(self, nome, extensao, tamanho, data_criacao, data_atualizacao):
        self.__nome = nome
        self.__tipo = extensao
        self.__tamanho = tamanho
        self.__data_criacao = data_criacao
        self.__data_atualizacao = data_atualizacao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho

    @property
    def data_criacao(self):
        return self.__data_criacao

    @data_criacao.setter
    def tamanho(self, data_criacao):
        self.__data_criacao = data_criacao

    @property
    def data_atualizacao(self):
        return self.__data_atualizacao

    @data_atualizacao.setter
    def data_atualizacao(self, data_atualizacao):
        self.__data_atualizacao = data_atualizacao
