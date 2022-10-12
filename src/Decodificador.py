from tkinter import *
from ttkbootstrap import Style
import json
import re
import sys
import keyword
from os.path import dirname, join

from Sistema import Sistema


class Decodificador:
    def __init__(self, master = None):
        # self.widgetPy = textPy
        # self.widgetRun = textRun
        self.tela = master

        self.sistema = Sistema()

    def exibirTela(self):
        print('Classe:Login - exibirTela')
        # self.encontrar.exibirTela()
        self.editor.exibirTela()
    def codificadorParaPython(self, codigo):
        return self.codificacao(codigo, compilacao=True)

    def codificacao(self, code, **options):
        compilacao = options.get('compilacao')

        #essa parte ira indentificar todos os aspas simples e duplos presentes no arquivo
        variaveis = []
        for x in range(len(code)):
            if code[x] == "'" or code[x] == '"':
                variaveis.append(x)

        #essa parte ira agrupar em duplas todos as aspas simples ou duplas do codigo e criarndo um codigo para cada dupla de aspas
        imutaveis = []
        for y in range(0, len(variaveis), 2):
            try:
                imutaveis.append(
                    ['000' + str(y), [variaveis[y], variaveis[y + 1] + 1]])
            except:
                print('erro de sintaxe')

        # essa parte sera responsavel por subistituir os strings pelos codigos criados
        codigoAlt = code
        for r in range(len(imutaveis)):
            codigoAlt = codigoAlt.replace(
                code[imutaveis[r][1][0]:imutaveis[r][1][1]], str(imutaveis[r][0]),
                1)

        # essa parte sera responsavel por subistituir os comandos PortoPy por os comandos python
        if compilacao == True or compilacao == None:
            codigoAlt = self.reposicionar(codigoAlt, True)
        else:
            codigoAlt = self.reposicionar(codigoAlt, False)

        #essa parte sera responsavel por subistiuir os codigos criados por seus respectivos valores
        final = codigoAlt
        for r in range(len(imutaveis)):
            final = final.replace(str(imutaveis[r][0]),
                                  code[imutaveis[r][1][0]:imutaveis[r][1][1]], 1)
        return final
    def criarArquivoTemporario(self, conteudo):
        local_padrao = str(self.sistema.pasta_do_app+'/temp.py')
        temp = open(local_padrao, 'w')
        temp.write(conteudo)
        temp.close()
        return local_padrao


    def reposicionar(self, script, comp):
        try:
          current_dir = dirname(__file__)
          file_path = join(current_dir, "./comandos.json")
          with open(file_path, 'r', encoding="utf-8") as reservados:
              obj = json.loads(reservados.read())
        except FileNotFoundError as erro:
            sys.exit()
        else:
            comandos = obj['keyword']
            script2 = script
            for x in range(len(comandos)):
                if not comp:
                    #Python para portoPy
                    text = re.findall(r"\b" +comandos[x][0]+r'\s', script2)
                    for r in range(len(text)):
                        if text[r][-1:]== '\n':
                            a = comandos[x][1]+'\n'
                        else:
                            a = comandos[x][1]+' '
                        script2 = re.sub(r"\b" +comandos[x][0]+r'\s', a, script2)
                else:
                    #portoPy para Python
                    text = re.findall(r"\b" +comandos[x][1]+r'\s', script2)
                    for r in range(len(text)):
                        if text[r][-1:]== '\n':
                            a = comandos[x][0]+'\n'
                        else:
                            a = comandos[x][0]+' '
                        script2 = re.sub(r"\b" +comandos[x][1]+r'\s', a, script2)
            comandos = obj['dir']
            for x in range(len(comandos)):
                if not comp:
                    #Python para portoPy
                    script2 = re.sub(r"\b" + comandos[x][0] + r"\b", comandos[x][1], script2)
                else:
                    #portoPy para Python
                    script2 = re.sub(r"\b" + comandos[x][1] + r"\b", comandos[x][0], script2)
            comandos = obj['listas']
            for x in range(len(comandos)):
                if not comp:
                    #Python para portoPy
                    script2 = re.sub(r"." + comandos[x][0] + r"\b", "."+comandos[x][1], script2)
                else:
                    #portoPy para Python
                    script2 = re.sub(r"." + comandos[x][1] + r"\b", "."+comandos[x][0], script2)
            return script2

if __name__ == '__main__':
  pass
