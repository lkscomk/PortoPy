from tkinter import *
from tkinter.font import BOLD
from ttkbootstrap import Style

# This is a scrollable text widget
class EncontrarSubstituir:
    def __init__(self, master, text):
        self.tela = master
        self.text =text
        self.conteiner_1 = Frame(master)
        self.cor_de_tela = None
        self.cor_primaria = None
        self.cor_segundaria = None
        self.cor_danger = None
        self.cor_inputfg = None
        self.cor_success = None
        self.font_padrao = ('courier new', 11, BOLD)

        self.organizar_cores()

        self.frame = Frame(self.tela)
        self.editFrame = Label(self.frame, text='Find').pack(side=LEFT)
        self.edit = Entry(self.frame)
        self.Find = Button(self.frame, text='Find')
        self.edit2Frame = Label(self.frame, text="Replace With ").pack(side=LEFT)
        self.edit2 = Entry(self.frame)
        self.replace = Button(self.frame, text='FindNReplace')
        self.refresh = Button(self.frame, text='Refresh')

        self.Find.config(command=self.find)
        self.replace.config(command=self.findNreplace)
        self.refresh.config(command=self.refresh_func)
        # binding entry boxes ...
        self.edit.bind('<Return>', self.find)
        self.edit2.bind('<Return>', self.findNreplace)

    def ocultarTela(self):
        self.edit.pack_forget()
        self.Find.pack_forget()
        self.edit2.pack_forget()
        self.replace.pack_forget()
        self.refresh.pack_forget()
        self.frame.pack_forget()

    def exibirTela(self, objeto =  None):
        self.edit.pack(side=LEFT, fill=BOTH, expand=1)
        self.edit.focus_set()
        self.Find.pack(side=LEFT)
        self.edit2.pack(side=LEFT, fill=BOTH, expand=1)
        self.edit2.focus_set()
        self.replace.pack(side=LEFT)
        self.refresh.pack(side=LEFT)
        t = objeto.conteiner_1 if objeto != None else None #quando for para colocar em um local especifico
        self.frame.pack(side=TOP, before=t)

    def find(self, *args):
      # remove tag 'found' from index 1 to END
      self.text.tag_remove('found', '1.0', END)

      # returns to widget currently in focus
      s = self.edit.get()

      if (s):
          idx = '1.0'
          while 1:
              # searches for desried string from index 1
              idx = self.text.search(s, idx, nocase=1,
                                stopindex=END)

              if not idx: break
              # last index sum of current index and
              # length of text
              lastidx = '% s+% dc' % (idx, len(s))
              # overwrite 'Found' at idx
              self.text.tag_add('found', idx, lastidx)
              idx = lastidx

          # mark located string as green and bg = ''yellow
          self.text.tag_config('found', foreground='green', background='yellow')
      self.edit.focus_set()


    def findNreplace(self, *args):
        # remove tag 'found' from index 1 to END
        self.text.tag_remove('found', '1.0', END)

        # returns to widget currently in focus
        s = self.edit.get()
        r = self.edit2.get()

        if (s and r):
            idx = '1.0'
            while 1:
                # searches for desried string from index 1
                idx = self.text.search(s, idx, nocase=1,
                                  stopindex=END)
                if not idx: break

                # last index sum of current index and
                # length of text
                lastidx = '% s+% dc' % (idx, len(s))

                self.text.delete(idx, lastidx)
                self.text.insert(idx, r)

                lastidx = '% s+% dc' % (idx, len(r))

                # overwrite 'Found' at idx
                self.text.tag_add('found', idx, lastidx)
                idx = lastidx

            # mark located string as green and bg = ''yellow
            self.text.tag_config('found', foreground='green', background='yellow')
        self.edit.focus_set()

    def refresh_func(self):
        self.text.tag_delete('found')


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

if __name__ == '__main__':
    root = Tk()
    text = Text(root)
    text.pack(side=BOTTOM)
    tela = EncontrarSubstituir(root, text)
    tela.exibirTela()
    root.mainloop()
