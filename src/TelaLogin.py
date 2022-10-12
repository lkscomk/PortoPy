import tkinter as tk
import tkinter.font as tkFont
from ttkbootstrap import Style
import ttkbootstrap as ttk

class Login:
    def __init__(self, master=None):
        self.tela = master

        self.cor_de_tela = None
        self.cor_primaria = None
        self.cor_segundaria = None
        self.cor_danger = None
        self.cor_inputfg = None
        self.cor_success = None
        self.font_padrao = ('helvetica', 9)

        self.emailEntry=ttk.Entry(self.tela)
        self.senhaEntry=ttk.Entry(self.tela)
        self.GLabel_198=tk.Label(self.tela)
        self.GLabel_236=tk.Label(self.tela)
        self.GLabel_306=tk.Label(self.tela)
        self.GButton_876=ttk.Button(self.tela)
        self.GButton_470=ttk.Button(self.tela)

    def exibirTela(self):
        self.tela.resizable(False, False)

        self.emailEntry.place(x=530,y=380,width=260,height=40)

        self.senhaEntry.place(x=530,y=270,width=260,height=40)

        self.GLabel_198["fg"] = "#333333"
        self.GLabel_198["justify"] = "center"
        self.GLabel_198["text"] = "Email"
        self.GLabel_198["font"] = ('calibri', 12)
        self.GLabel_198.place(x=515,y=230,width=70,height=25)


        self.GLabel_236["fg"] = "#333333"
        self.GLabel_236["justify"] = "center"
        self.GLabel_236["text"] = "Senha"
        self.GLabel_236["font"] = ('calibri', 12)
        self.GLabel_236.place(x=515,y=330,width=70,height=25)


        self.GLabel_306["fg"] = "#333333"
        self.GLabel_306["justify"] = "center"
        self.GLabel_306["text"] = "PortPy"
        self.GLabel_306["font"] = ('calibri', 28)
        self.GLabel_306.place(x=510,y=60,width=308,height=98)


        self.GButton_470["text"] = "Entrar"
        self.GButton_470.place(x=530,y=460,width=120,height=30)
        self.GButton_470["command"] = self.GButton_470_command

        self.GButton_876["text"] = "cadastre - se"
        self.GButton_876.place(x=670,y=460,width=123,height=30)
        self.GButton_876["command"] = self.GButton_876_command

    def GButton_470_command(self):
        print("command")


    def GButton_876_command(self):
        print("command")

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

if __name__ == "__main__":
    root = tk.Tk()
    tela = Login(root)
    tela.exibirTela()
    root.mainloop()
