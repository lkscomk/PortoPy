from tkinter import *
from ttkbootstrap import Style
from Decodificador import Decodificador
from EncontrarSubstituir import EncontrarSubstituir
from ComponenteEditor import Editor
from Run import Maquina
from tkinter import font, filedialog
from tkinter import messagebox as mbox
import os




class Ambiente:
    def __init__(self, master=None):
        self.tela = master

        self.editor = Editor(master)
        self.editorPy = Editor(master)
        self.encontrar = EncontrarSubstituir(master, self.editor.text)
        self.decodificador = Decodificador()
        self.run = Maquina()

        self.editor.text.bind('<<Modified>>', self.codificarParaPython)

        self.cor_de_tela = None
        self.cor_primaria = None
        self.cor_segundaria = None
        self.cor_danger = None
        self.cor_inputfg = None
        self.cor_success = None
        self.font_padrao = ('helvetica', 9)
        self.organizar_cores()

        self.mainmenu = Menu(master)
        self.filemenu1 = Menu(self.mainmenu)
        self.filemenu2 = Menu(self.mainmenu)
        self.filemenu3 = Menu(self.mainmenu)
        self.filemenu1.add_command(label="Open")
        self.filemenu1.add_command(label="Save as")
        self.filemenu1.add_separator()
        self.filemenu1.add_command(label="Exit", command=quit)
        self.mainmenu.add_cascade(label="File", menu=self.filemenu1)

        self.filemenu2.add_command(label="Procurar", command=self.abrirOpcaoEncontrar)
        self.filemenu2.add_command(label="Ver tela Python", command=self.abrirOpcaoTelaPython)
        self.filemenu2.add_separator()
        self.mainmenu.add_cascade(label="Editar", menu=self.filemenu2)

        self.filemenu3.add_command(label="Run", command=self.rodarCodigo)
        self.filemenu3.add_separator()
        self.mainmenu.add_cascade(label="Run", menu=self.filemenu3)

        self.opcaoEncontrar = False
        self.opcaoTelaPython = False

    def exibirTela(self):
        print('Classe:Login - exibirTela')
        self.editor.exibirTela()
        self.tela.config(menu=self.mainmenu)

    def ocultarTela(self):
        print('Classe:Login - ocultarTela')
        self.editor.ocultarTela()

    def codificarParaPython(self, *args):
        self.editor.text.edit_modified(0)
        codigo = self.editor.text.get("1.0", "end-1c")
        resultado = self.decodificador.codificadorParaPython(codigo)
        self.editorPy.text.delete("1.0", "end-1c")
        self.editorPy.text.insert(END, resultado)

    def abrirOpcaoEncontrar(self):
        self.opcaoEncontrar = False if self.opcaoEncontrar else True
        self.encontrar.exibirTela(self.editor) if self.opcaoEncontrar else self.encontrar.ocultarTela()

    def abrirOpcaoTelaPython(self):
        self.opcaoTelaPython = False if self.opcaoTelaPython else True
        self.editorPy.exibirTela(self.editor) if self.opcaoTelaPython else self.editorPy.ocultarTela()

    def rodarCodigo(self):
        codigo = self.editor.text.get("1.0", "end-1c")
        resultado = self.decodificador.codificadorParaPython(codigo)
        self.run.iniciacaoRun(resultado)


    def organizar_cores(self):
        print('Classe:Login - organizar_cores')

        self.style = Style()
        self.style.configure('TButton', font=self.font_padrao)

        self.cor_bg = self.style.colors.get('bg')
        self.cor_primary = self.style.colors.get('primary')
        self.cor_secondary = self.style.colors.get('secondary')
        self.cor_danger = self.style.colors.get('danger')
        self.cor_inputbg = self.style.colors.get('inputbg')
        self.cor_inputfg = self.style.colors.get('inputfg')
        self.cor_success = self.style.colors.get('success')

if __name__ == '__main__':
  root = Tk()
  tela = Ambiente(root)
  tela.exibirTela()
  root.mainloop()
