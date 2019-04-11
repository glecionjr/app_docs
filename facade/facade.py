# Controle de transacao
# Obter sessao
# Com a sessao, faz commit e rollback
# Chamar as ações de negocio

from negocio import boarquivo

class Facade():

    def download_arquivo(self, url):
        bo = boarquivo.BOArquivo()
        bo.download_arquivos(url)

    def regitrar_metadados(self, arquivo):
        pass

    def baixar_arq_registrar_metadado(self, url, arquivo):
        # download
        # registrar metadados
        pass
