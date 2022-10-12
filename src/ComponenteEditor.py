import tkinter as tk
from tkinter.font import BOLD
from idlelib.idle_test.test_colorizer import source
from idlelib.percolator import Percolator
from ttkbootstrap import Style
import socketio

try:
    from .Colorizer import *
except:
    from Colorizer import *

import tkinter as tk


# This is a scrollable text widget
class Editor:
    def __init__(self, master):
        self.tela = master
        self.conteiner_1 = Frame(master)
        self.cor_de_tela = None
        self.cor_primaria = None
        self.cor_segundaria = None
        self.cor_danger = None
        self.cor_inputfg = None
        self.cor_success = None
        self.font_padrao = ('courier new', 11, BOLD)

        self.organizar_cores()

        self.text = tk.Text(self.conteiner_1, width=100, height=100, font=self.font_padrao)
        color_config(self.text)
        p = Percolator(self.text)
        d = ColorDelegator()
        p.insertfilter(d)

        self.scrollbar = tk.Scrollbar(self.text, orient=tk.VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        self.numberLines = TextLineNumbers(self.conteiner_1, width=40, bg="#606366")
        self.numberLines.attach(self.text)

        self.text.bind("<Key>", self.onPressDelay)
        self.text.bind("<Button-1>", self.numberLines.redraw)
        self.scrollbar.bind("<Button-1>", self.onScrollPress)
        self.text.bind("<MouseWheel>", self.onPressDelay)
        """  
        def enviar(event):
            master.after(1, lambda: OnKeyPress())

        self.text.bind("<KeyPress>", enviar)
        # conexão

        self.sio = socketio.Client()

        @self.sio.event(namespace='/chat')
        def connect():
            print('connection established')

        @self.sio.event
        def OnKeyPress():
            res = self.text.get("1.0", "end-1c")
            nome = 'ed'
            self.sio.emit('message', nome+': '+res, namespace='/chat')

        @self.sio.event(namespace='/chat')
        def broadcast_chat(data):
            nome = 'ed'
            quem = data.split(': ')[0]
            if quem != nome:
                self.text.delete("1.0", "end-1c")
                print(type(data))
                self.text.insert(END, str(data.replace(quem+': ','')))

        @self.sio.event
        def disconnect():
            print('disconnected from server')

        self.sio.connect('https://repl-chat-server.lukasrocha.repl.co?nome=lukas', namespaces=['/chat'])
        """



    def exibirTela(self, objeto = None):
        t = objeto.conteiner_1 if objeto != None else None #quando for para colocar em um local especifico
        self.conteiner_1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, after=t)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.numberLines.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def ocultarTela(self):
        self.conteiner_1.pack_forget()
        self.scrollbar.pack_forget()
        self.numberLines.pack_forget()
        self.text.pack_forget()

    def organizar_cores(self):
        print('Classe:App - organizar_cores')

        self.style = Style()
        self.style.configure('TButton', font=self.font_padrao)

        self.cor_bg = self.style.colors.get('bg')
        self.cor_primary = self.style.colors.get('primary')
        self.cor_secondary = self.style.colors.get('secondary')
        self.cor_danger = self.style.colors.get('danger')
        self.cor_inputbg = self.style.colors.get('inputbg')
        self.cor_inputfg = self.style.colors.get('inputfg')
        self.cor_success = self.style.colors.get('success')

    def onScrollPress(self, *args):
        self.scrollbar.bind("<B1-Motion>", self.numberLines.redraw)

    def onScrollRelease(self, *args):
        self.scrollbar.unbind("<B1-Motion>", self.numberLines.redraw)

    def onPressDelay(self, *args):
        self.tela.after(2, self.numberLines.redraw)

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def redraw(self):
        self.numberLines.redraw()

class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum, fill="#000000")
            i = self.textwidget.index("%s+1line" % i)

if __name__ == '__main__':
    root = tk.Tk()
    tela = Editor(root)
    tela.exibirTela()
    root.mainloop()
