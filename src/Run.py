import win32gui
import win32con
import os, sys, time


class Maquina:
  def __init__(self):
    self.the_program_to_hide = win32gui.GetForegroundWindow()
    # win32gui.ShowWindow(self.the_program_to_hide, win32con.SW_HIDE)
  def limparTelaConsole(self):
    os.system('cls') or None
  def colocarTextosIniciais(self):
    exec(r"print('Python %s\n' % sys.version)")
  def mostrarTelaConsole(self):
    # win32gui.ShowWindow(self.the_program_to_hide, win32con.SW_SHOW)
    pass
  def runCod(self, cod):
    try:
      exec(cod)
    except SyntaxError as erro:
      print('erro de sintaxe', erro)
  def iniciacaoRun(self, cod):
    self.mostrarTelaConsole()
    self.limparTelaConsole()
    self.colocarTextosIniciais()
    self.runCod(cod)
    time.sleep(2)
    #win32gui.ShowWindow(self.the_program_to_hide, win32con.SW_HIDE)



if __name__ == '__main__':
  pass
