from datetime import *
from pathlib import Path
from time import strftime

class Sistema:
    def __init__(self):
        self.data = self.criar_data()
        self.local_app = self.criar_local_app()
        self.pasta_do_app = self.criar_pasta_app()
        self.local_bando_dados = self.criar_local_banco()
        self.local_imagens = self.criar_local_imagens_arquivos()
        self.local_canche = self.criar_cache()

    def criar_data(self):
        print('Classe:Sistema - criar_data')
        data_atual = str(date.today())
        dia = data_atual[8:10]
        mes = data_atual[5:7]
        ano = data_atual[0:4]
        return (dia + '/' + mes + '/' + ano)

    def criar_local_app(self):
        print('Classe:Sistema - criar_local_app')
        import os.path
        cwd = os.path.expanduser("~\AppData\Local\Programs")
        return cwd

    def criar_pasta_app(self):
        print('Classe:Sistema - criar_pasta_app')
        d = self.local_app + r'\PortuPy'
        Path(d).mkdir(exist_ok=True)
        return d

    def criar_local_banco(self):
        print('Classe:Sistema - criar_local_banco')
        e = self.pasta_do_app + r'\Banco_de_dados'
        Path(e).mkdir(exist_ok=True)
        return e

    def criar_local_imagens_arquivos(self):
        print('Classe:Sistema - criar_local_imagens_arquivos')
        e = self.pasta_do_app + r'\Imagens'
        Path(e).mkdir(exist_ok=True)
        return e

    def criar_cache(self):
        print('Classe:Sistema - criar_cache')
        e = self.local_bando_dados + r'\Cache'
        Path(e).mkdir(exist_ok=True)
        return e

    def criar_hora(self):
        print('Classe:Sistema - criar_hora')
        a = strftime("%H:%M:%S")
        return str(a)


if __name__ == '__main__':
    sistema = Sistema()
    print(sistema.criar_local_app())
    print(sistema.criar_pasta_app())
    print(sistema.criar_local_banco())
    print(sistema.criar_local_imagens_arquivos())
    print(sistema.criar_cache())
    print(sistema.criar_hora())
