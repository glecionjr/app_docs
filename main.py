from facade import facade

# def main():
try:
    url = input("Informe a URL para baixar arquivos: ")

    fachada = facade.Facade()
    arqs = fachada.download_arquivos(url)
    fachada.regitrar_metadados()

except Exception as e:
    print(e)

# Executa somente como script. Se for importado, não executa
if __name__ == "main":
     pass
