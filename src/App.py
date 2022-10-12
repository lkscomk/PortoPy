from ttkbootstrap import Style
from ttkbootstrap import icons
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from TelaPrincipal import Ambiente
from TelaLogin import Login
from TelaInicial import Incial

class App:
    def __init__(self, master=None):
        self.tela = master
        self.largura = 1360
        self.altura = 768

        # resoução screen
        self.largura_screen = self.tela.winfo_screenwidth()
        self.altura_screen = self.tela.winfo_screenheight()

        # posição
        self.posx = self.largura_screen / 2 - self.largura / 2
        self.posy = self.altura_screen / 2 - self.altura / 2

        self.tela.minsize(500, 500)
        # master.state('zoomed')
        self.tela.geometry('%dx%d+%d+%d' % (self.largura, self.altura, self.posx, self.posy))
        self.tela.title('Umbrella Stores (beta - V.0.1)')

        self.inicial = Incial(master)
        self.idle = Ambiente(master)
        self.login = Login(master)

        self.inicial.exibirTela()
        self.inicial.codificar['command'] = self.abrir_telaCodificar
        self.inicial.sair['command'] = quit




        # self.login.exibirTela()
        # self.login.ocultarTela()
        # self.inicial.ocultarTela()
        # self.idle.exibirTela()
        # self.idle.ocultarTela()

        self.cor_de_tela = None
        self.cor_primaria = None
        self.cor_segundaria = None
        self.cor_danger = None
        self.cor_inputfg = None
        self.cor_success = None
        self.font_padrao = ('helvetica', 9)
        self.name_style = ''
        self.organizar_cores()

    def abrir_telaCodificar(self):
        self.inicial.ocultarTela()
        self.idle.exibirTela()

    def organizar_cores(self):
        print('Classe:App - organizar_cores')

        self.style = Style(self.name_style)
        self.style.configure('TButton', font=self.font_padrao)

        self.cor_bg = self.style.colors.get('bg')
        self.cor_primary = self.style.colors.get('primary')
        self.cor_secondary = self.style.colors.get('secondary')
        self.cor_danger = self.style.colors.get('danger')
        self.cor_inputbg = self.style.colors.get('inputbg')
        self.cor_inputfg = self.style.colors.get('inputfg')
        self.cor_success = self.style.colors.get('success')

        self.inicial.organizar_cores()
        self.login.organizar_cores()

if __name__ == '__main__':
    root = ttk.Window()
    app = App(root)
    root.mainloop()
