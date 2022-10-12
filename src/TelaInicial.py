import ttkbootstrap as ttk
from tkinter import *
from ttkbootstrap import Style

try:
    from .Sistema import *
except:
    from Sistema import *

class Incial:
    def __init__(self, master):
        self.tela = master
        self.sistema = Sistema()

        self.cor_de_tela = None
        self.cor_primaria = None
        self.cor_segundaria = None
        self.cor_danger = None
        self.cor_inputfg = None
        self.cor_success = None
        self.font_padrao = ('helvetica', 9)

        self.conteiner_1_st = Frame(master)
        self.conteiner_2_st = Frame(master)
        self.conteiner_3_st = Frame(master)


        self.portoPy = Label(self.conteiner_1_st)
        self.codificar = ttk.Button(self.conteiner_2_st)
        self.sala = ttk.Button(self.conteiner_2_st)
        self.ajuda = ttk.Button(self.conteiner_2_st)
        self.sair = ttk.Button(self.conteiner_2_st)
        self.sobre = Label(self.conteiner_3_st)
    def exibirTela(self):
        print('Classe:Incial - exibirTela')
        self.tela.resizable(False, False)
#
        self.conteiner_1_st.pack(fill="both")
        self.conteiner_2_st.pack(fill="both")
        self.conteiner_3_st.pack(side=BOTTOM, fill="both")


        self.portoPy['text'] = 'Bem vindo ao IGPy'
        self.portoPy['font'] = ('Calibri', 30, 'bold')
        self.portoPy['bg'] = self.cor_danger
        self.portoPy.pack(ipady=10, pady=20, fill='both')

        self.codificar['text'] = 'Criar arquivo'
        self.codificar['width'] = 40
        self.codificar.pack(pady=3)

        self.sala['text'] = 'Entrar em sala'
        self.sala['width'] = 40
        self.sala.pack(pady=3)

        self.ajuda['text'] = 'Documentação'
        self.ajuda['width'] = 40
        self.ajuda.pack(pady=3)

        self.sair['text'] = 'Sair'
        self.sair['width'] = 40
        self.sair.pack(pady=3)

        self.sobre['text'] = 'Desenvolvido por lkscomk'
        self.sobre.pack(pady=20)
    def ocultarTela(self):
        print('Classe:Incial - ocultarTela')
        self.conteiner_1_st.pack_forget()
        self.conteiner_2_st.pack_forget()
        self.conteiner_3_st.pack_forget()
        self.portoPy.pack_forget()
        self.codificar.pack_forget()
        self.sala.pack_forget()
        self.ajuda.pack_forget()
        self.sair.pack_forget()
        self.sobre.pack_forget()
    def organizar_cores(self):
        print('Classe:Incial - organizar_cores')

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
    root = ttk.Window()
    app = Incial(root)
    app.exibirTela()
    app.organizar_cores()
    root.mainloop()
