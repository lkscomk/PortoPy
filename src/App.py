from tkinter import *
from ttkbootstrap import Style
from Decodificador import Decodificador
from EncontrarSubstituir import EncontrarSubstituir
from ComponenteEditor import Editor
from Run import Maquina
import webbrowser
import sys
from tkinter import filedialog
from tkinter import messagebox
import base64

class App:
    def __init__(self, master=None):
        self.tela = master
        self.tela.protocol("WM_DELETE_WINDOW", self.fechar_janela)

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
        self.tela.geometry('%dx%d+%d+%d' %
                           (self.largura, self.altura, self.posx, self.posy))
        self.arquivo = ''
        self.arquivoSalvo = True
        self.tela.title(f'PortuPy (beta - V.0.1) - Nenhum arquivo aberto')

        image_data = base64.b64decode('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')
        self.icon = PhotoImage(data=image_data)
        self.tela.tk.call('wm', 'iconphoto', self.tela._w, self.icon)

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
        self.filemenu4 = Menu(self.mainmenu)
        self.filemenu1.add_command(
            label="Abrir (Ctrl + O)", command=self.perguntar_salvar)
        self.tela.bind("<Control-o>", self.perguntar_salvar)
        self.filemenu1.add_command(
            label="Salvar (Ctrl + S)", command=self.salvar_em_arquivo)
        self.tela.bind("<Control-s>", self.salvar_em_arquivo)
        self.filemenu1.add_separator()
        self.filemenu1.add_command(label="Sair", command=sys.exit)
        self.mainmenu.add_cascade(label="Arquivo", menu=self.filemenu1)

        self.filemenu2.add_command(label="Procurar (Ctrl + F)", command=self.abrirOpcaoEncontrar)
        self.tela.bind("<Control-f>", self.abrirOpcaoEncontrar)
        self.filemenu2.add_command(label="Ocultar/Mostrar tela Python (Ctrl + D)", command=self.abrirOpcaoTelaPython)
        self.tela.bind("<Control-d>", self.abrirOpcaoTelaPython)
        self.filemenu2.add_command(label="Converter Para PortoPy (Ctrl + K)", command=self.codificarParaPortoPy)
        self.tela.bind("<Control-k>", self.codificarParaPortoPy)
        self.filemenu2.add_separator()
        self.filemenu2.add_command(label="Aumentar Fonte (Ctrl +)", command=self.aumentar_fonte)
        self.tela.bind("<Control-plus>", self.aumentar_fonte)
        self.filemenu2.add_command(label="Diminuir Fonte (Ctrl -)", command=self.diminuir_fonte)
        self.tela.bind("<Control-minus>", self.diminuir_fonte)
        self.filemenu2.add_command(label="Desfazer (Ctrl + Z)", command=self.desfazer)
        self.tela.bind("<Control-z>", self.desfazer)
        self.filemenu2.add_command(label="Refazer (Ctrl + Shitf + Z)", command=self.refazer)
        self.tela.bind("<Control-Shift-Z>", self.refazer)
        self.filemenu2.add_command(label="Ajustar Indentação (Ctrl + B)", command=self.ajustar_indentacao)
        self.tela.bind("<Control-b>", self.ajustar_indentacao)
        self.mainmenu.add_cascade(label="Editar", menu=self.filemenu2)

        self.filemenu3.add_command(label="Run (F5)", command=self.rodarCodigo)
        self.tela.bind("<F5>", self.rodarCodigo)
        self.mainmenu.add_cascade(label="Rodar", menu=self.filemenu3)

        self.filemenu4.add_command(label="Documentação", command=self.abrirDocumentacao)
        self.mainmenu.add_cascade(label="Ajuda", menu=self.filemenu4)

        self.opcaoEncontrar = False
        self.opcaoTelaPython = True
        self.exibirTela()

    def ajustar_indentacao(self, event=None):
        codigo = self.editorPy.ajustar_indentacao(self.editorPy.text.get("1.0", "end-1c"))
        print(codigo)
        self.editorPy.text.delete("1.0", "end-1c")
        self.editorPy.text.insert(END, codigo)
        self.codificarParaPortoPy()

    def desfazer(self, event=None):
        self.editor.desfazer()
        self.editorPy.desfazer()

    def refazer(self, event=None):
        self.editor.refazer()
        self.editorPy.refazer()

    def aumentar_fonte(self, event=None):
        self.editor.aumentar_fonte()
        self.editorPy.aumentar_fonte()

    def diminuir_fonte(self, event=None):
        self.editor.diminuir_fonte()
        self.editorPy.diminuir_fonte()

    def exibirTela(self):
        print('Classe:App - exibirTela')
        self.editor.exibirTela()
        self.editorPy.exibirTela(self.editor)
        self.tela.config(menu=self.mainmenu)

    def abrirDocumentacao(self, event=None):
        conteudo_html = """<!DOCTYPE html>
<html>

<head>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f0f0f0;
      margin: 0;
      padding: 20px;
    }

    h1 {
      color: #333;
    }

    p {
      margin: 10px 0;
    }

    code {
      background-color: #f5f5f5;
      padding: 2px 6px;
      border: 1px solid #ccc;
    }

    .section {
      background-color: #fff;
      border: 1px solid #ccc;
      padding: 20px;
      margin: 10px 0;
      border-radius: 5px;
    }

    .code-example {
      background-color: #f5f5f5;
      padding: 10px;
      border: 1px solid #ccc;
      margin: 10px 0;
    }
  </style>
</head>

<body>
  <h1>Documentação Básica</h1>

  <div class="section">
    <h2>Proposta PortuPy</h2>
    <p>
      O PortuPy é uma pseudolinguagem que foi
      criada com o propósito de ensinar os conceitos fundamentais da programação de uma forma divertida e acessível,
      especialmente para estudantes iniciantes.
    </p>
    <p>
      PortuPy tem sua sintaxe semelhante a do Python (linguagem de programação real, muito usada no mercado).
      O objetivo do uso dessa pseudolinguagem é que futuramente o aluno progride para uma linguagem de programação,
      nesse caso, preferenciamento, o Python, pela sua facilidade de aprendizado. Essa ferramenta usa palavras em
      português para representar comandos de programação, o que o torna mais acessível para pessoas
      que falam a língua portuguesa. Isso é ótimo para iniciantes, pois elimina a barreira do idioma.
    </p>
    <p>
      Além disso, mesmo sendo uma pseudolinguagem, o PortuPy é projetado para ensinar conceitos fundamentais de
      programação, como variáveis, estruturas condicionais, loops e funções. Os estudantes podem aprender esses
      conceitos de forma interativa e prática.
    </p>
    <p>
      Em resumo, o PortuPy é uma pseudolinguagem de programação que se destaca por sua simplicidade e acessibilidade.
      Ele é uma ferramenta valiosa para aqueles que estão dando os primeiros passos na programação e desejam entender os
      conceitos básicos de uma forma amigável e envolvente. Se você está começando a estudar programação, o PortuPy pode
      ser uma introdução divertida e educativa a este mundo fascinante.
    </p>
  </div>

  <div class="section">
    <h2>Comandos de Entrada e Saída</h2>
    <p>Para receber entrada do usuário em PortuPy, você pode usar a função <code>entrada()</code>:</p>
    <div class="code-example">
      <pre>
nome = entrada("Digite seu nome: ")
      </pre>
    </div>
    <p>Para exibir saída, use a função <code>escrever()</code>:</p>
    <div class="code-example">
      <pre>
escrever("Olá, " + nome)
      </pre>
    </div>
  </div>

  <div class="section">
    <h2>Principais Tipos de Dados</h2>
    <p>Python suporta diversos tipos de dados, incluindo:</p>
    <ul>
      <li>Números inteiros (inteiro)</li>
      <li>Números decimais (decimal)</li>
      <li>Carateres (caracter)</li>
      <li>Lógicos (logico)</li>
    </ul>
    <div class="code-example">
      <pre>
#caracter
nome = "Joao"

#inteiro
idade = 15

#decimal
altura = 1.75

#logico
trabalha = Verdadeiro
      </pre>
    </div>
  </div>

  <div class="section">
    <h1>Operadores em PortuPy</h1>

    <div class="section">
      <h2>Operadores Aritméticos</h2>
      <ul>
        <li><code>+</code> (Adição)</li>
        <li><code>-</code> (Subtração)</li>
        <li><code>*</code> (Multiplicação)</li>
        <li><code>/</code> (Divisão)</li>
        <li><code>//</code> (Divisão de Inteira)</li>
        <li><code>%</code> (Módulo - Resto da Divisão)</li>
        <li><code>**</code> (Exponenciação)</li>
      </ul>
    </div>

    <div class="section">
      <h2>Operadores de Comparação</h2>
      <ul>
        <li><code>==</code> (Igual a)</li>
        <li><code>!=</code> (Diferente de)</li>
        <li><code>&lt;</code> (Menor que)</li>
        <li><code>&gt;</code> (Maior que)</li>
        <li><code>&lt;=</code> (Menor ou igual a)</li>
        <li><code>&gt;=</code> (Maior ou igual a)</li>
      </ul>
    </div>

    <div class="section">
      <h2>Operadores Lógicos</h2>
      <ul>
        <li><code>and</code> (E lógico)</li>
        <li><code>or</code> (Ou lógico)</li>
        <li><code>not</code> (Negação lógica)</li>
      </ul>
    </div>

    <div class="section">
      <h2>Operadores de Identidade</h2>
      <ul>
        <li><code>is</code> (É)</li>
        <li><code>is not</code> (Não é)</li>
      </ul>
    </div>

    <div class="section">
      <h2>Operadores de Associação</h2>
      <ul>
        <li><code>in</code> (Está em)</li>
        <li><code>not in</code> (Não está em)</li>
      </ul>
    </div>

    <div class="section">
      <h2>Operadores de Atribuição</h2>
      <ul>
        <li><code>=</code> (Atribuição)</li>
        <li><code>+=</code> (Adição e atribuição)</li>
        <li><code>-=</code> (Subtração e atribuição)</li>
        <li><code>*=</code> (Multiplicação e atribuição)</li>
        <li><code>/=</code> (Divisão e atribuição)</li>
        <li><code>%=</code> (Módulo e atribuição)</li>
        <li><code>//=</code> (Divisão de Piso e atribuição)</li>
        <li><code>**=</code> (Exponenciação e atribuição)</li>
      </ul>
    </div>

    <div class="section">
      <h2>Operador de Concatenação de Strings</h2>
      <ul>
        <li><code>+</code> (Usado para concatenar strings)</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h1>Entendendo Estruturas de Condição</h1>

    <p>As estruturas de condição são usadas para criar lógica condicional em programas. Elas permitem que você tome
      decisões com base em condições específicas.</p>

    <h2>Exemplo de Estrutura de Condição:</h2>
    <div class="code-example">
      <pre>
# Solicita ao usuário que insira um número
numero = decimal(entrada("Digite um número: "))

# Verifica se o número é positivo
se numero > 0:
    escrever("O número é positivo.")
e se numero == 0:
    escrever("O número é zero.")
senao:
    escrever("O número é negativo.")

        </pre>
    </div>

    <p>Neste exemplo em Python, estamos verificando se a variável <code>idade</code> é maior ou igual a 18. Se a
      condição for verdadeira, o programa imprime "Você é maior de idade". Caso contrário, ele imprime "Você é menor de
      idade".</p>

    <h2>Principais Estruturas de Condição:</h2>
    <ul>
      <li><strong>se</strong>: Usado para verificar se uma condição é verdadeira.</li>
      <li><strong>e se</strong>: Permite verificar várias condições.</li>
      <li><strong>senao</strong>: Fornece uma alternativa caso a condição do <strong>se</strong> seja falsa.</li>
    </ul>

    <p>As estruturas de condição são fundamentais para criar programas que podem se adaptar a diferentes situações e
      tomar decisões com base em informações variáveis.</p>

  </div>

  <div class="section">
    <h1>Entendendo Estruturas de Repetição</h1>

    <p>As estruturas de repetição são usadas para executar um bloco de código várias vezes. Elas são essenciais para
      automatizar tarefas repetitivas em programas.</p>

    <h2>Estrutura de Repetição <code>para</code>:</h2>
    <div class="code-example">
      <pre>
nomes = ["Alice", "Bob", "Carol", "David"]
para nome em nomes:
    escrever("Olá, " + nome)
        </pre>
      <pre>
para x em faixa(10):
    escrever(x)
        </pre>
    </div>

    <p>Neste exemplo em Python, usamos um loop <code>para</code> para percorrer a lista de nomes e imprimir uma saudação
      para cada pessoa na lista.</p>

    <h2>Estrutura de Repetição <code>enquanto</code>:</h2>
    <div class="code-example">
      <pre>
contador = 0

enquanto contador &lt; 5:
    escrever("Contagem: " + caracter(contador))
    contador += 1
        </pre>
    </div>

    <p>Neste exemplo, usamos um loop <code>enquanto</code> para contar de 0 a 4. O loop continuará executando até que a
      condição <code>contador &lt; 5</code> seja falsa.</p>

    <p>As estruturas de repetição são cruciais para a automação e repetição de tarefas em programas, economizando tempo
      e esforço.</p>

  </div>

  <div class="section">
    <h1>Funções em Programação</h1>

    <p>Funções são blocos de código que podem ser reutilizados para realizar tarefas específicas. Elas ajudam a
      organizar e modularizar um programa.</p>

    <h2>Definindo e Chamando Funções:</h2>
    <div class="code-example">
      <pre>
# Definindo uma função
funcao saudacao(nome):
    devolva "Olá, " + nome

# Chamando a função
mensagem = saudacao("Alice")
escrever(mensagem)
        </pre>
    </div>

    <p>Neste exemplo em PortuPy, definimos uma função chamada `saudacao` que aceita um argumento `nome` e retorna uma
      mensagem de saudação. Em seguida, chamamos a função e armazenamos a mensagem resultante em uma variável.</p>

    <h2>Funções com Parâmetros Opcionais:</h2>
    <div class="code-example">
      <pre>
# Função com parâmetro opcional
funcao boas_vindas(nome, cidade="Desconhecida"):
    return "Olá, " + nome + " de " + cidade

# Chamando a função
mensagem = boas_vindas("Bob")
escrever(mensagem)
        </pre>
    </div>

    <p>Neste exemplo, a função `boas_vindas` aceita dois parâmetros, sendo que `cidade` tem um valor padrão opcional. Se
      a cidade não for fornecida, ela será definida como "Desconhecida" por padrão.</p>

    <p>As funções são uma parte fundamental da programação, permitindo a criação de blocos de código reutilizáveis para
      executar tarefas específicas.</p>

  </div>
  <div class="section">
    <h1>Tratamento de Exceções</h1>

    O tratamento de exceções é uma abordagem para lidar com erros de forma controlada. Utiliza blocos tentar e deuerro para
    envolver código que pode gerar exceções. Se uma exceção ocorrer, o controle é transferido para o bloco de exceção, onde
    é possível realizar ações específicas para lidar com o erro.

    <h2>Instrução Raise:</h2>
    A instrução raise é utilizada para gerar manualmente uma exceção. Isso é útil quando você deseja sinalizar um erro
    específico em determinada situação, permitindo um tratamento personalizado.
    <div class="code-example">
      <pre>
funcao exemplo_divisao(dividendo, divisor):
    tentar:
        se divisor == 0:
            errar ErroDeValor("Divisão por zero não é permitida.")
        resultado = dividendo / divisor
    deuerro ErroDeValor apelidar ve:
        escrever(f"Erro: {ve}")
    deuerro ErroDeTipo:
        escrever("Erro: Certifique-se de que os operandos são números.")
    senao:
        escrever("A divisão foi bem-sucedida. Resultado:", resultado)
    porfim:
        escrever("Esta parte sempre será executada, independentemente de haver uma exceção ou não.")

# Exemplos de uso
exemplo_divisao(10, 2)  # Saída esperada: A divisão foi bem-sucedida. Resultado: 5.0
exemplo_divisao(10, 0)  # Saída esperada: Erro: Divisão por zero não é permitida.
exemplo_divisao("10", 2)  # Saída esperada: Erro: Certifique-se de que os operandos são números.
        </pre>
    </div>
  </div>

  <div class="section">

    <h1>Palavras-chave e Comandos em Python</h1>
    <div class="code-example">
      <p><strong>Verdadeiro (True):</strong> Valor booleano verdadeiro.</p>
      <p><strong>Falso (False):</strong> Valor booleano falso.</p>
      <p><strong>semlocal (nonlocal):</strong> Indica uma variável não local.</p>
      <p><strong>continue (continue):</strong> Pula para a próxima iteração do loop.</p>
      <p><strong>porfim (finally):</strong> Bloco de código que é sempre executado, independentemente de exceções.</p>
      <p><strong>devolva (return):</strong> Retorna um valor de uma função.</p>
      <p><strong>deuerro (except):</strong> Bloco de código executado em caso de exceção.</p>
      <p><strong>importe (import):</strong> Importa um módulo ou pacote.</p>
      <p><strong>global (global):</strong> Indica uma variável global.</p>
      <p><strong>afirmar (assert):</strong> Verifica se uma expressão é verdadeira, gerando uma exceção se for falsa.
      </p>
      <p><strong>fazer (lambda):</strong> Cria funções anônimas.</p>
      <p><strong>classe (class):</strong> Define uma classe.</p>
      <p><strong>gerador (yield):</strong> Pausa uma função geradora e envia um valor para o chamador.</p>
      <p><strong>enquanto (while):</strong> Loop de repetição enquanto uma condição é verdadeira.</p>
      <p><strong>errar (raise):</strong> Levanta uma exceção.</p>
      <p><strong>quebrar (break):</strong> Sai de um loop.</p>
      <p><strong>e se (elif):</strong> Se a condição anterior for falsa, testa uma nova condição.</p>
      <p><strong>se (if):</strong> Testa uma condição.</p>
      <p><strong>senao (else):</strong> Bloco de código executado se a condição do "if" for falsa.</p>
      <p><strong>senao (else:):</strong> Bloco de código executado se a condição do "if" for falsa.</p>
      <p><strong>de (from):</strong> Importa partes específicas de um módulo.</p>
      <p><strong>Nada (None):</strong> Valor nulo.</p>
      <p><strong>passar (pass):</strong> Sentença nula (não faz nada).</p>
      <p><strong>com (with):</strong> Gerencia recursos usando um contexto.</p>
      <p><strong>para (for):</strong> Loop de repetição para iterar sobre uma sequência.</p>
      <p><strong>tentar (try:):</strong> Bloco de código onde exceções podem ocorrer.</p>
      <p><strong>funcao (def):</strong> Define uma função.</p>
      <p><strong>nao (not):</strong> Operador lógico de negação.</p>
      <p><strong>remova (del):</strong> Remove um item de uma coleção.</p>
      <p><strong>apelidar (as):</strong> Renomeia um módulo ou um objeto durante a importação.</p>
      <p><strong>ou (or):</strong> Operador lógico "ou".</p>
      <p><strong>em (in):</strong> Verifica se um valor está presente em uma sequência.</p>
      <p><strong>e (and):</strong> Operador lógico "e".</p>
      <p><strong>é (is):</strong> Verifica se dois objetos são o mesmo.</p>
    </div>
  </div>

  <div class="section">
    <h1>Comandos de Listas em PortuPy</h1>

    <div class="code-example">
      <h2>append - acrescentar</h2>
      <pre>
variavel = [1, 2, 3]
variavel.acrescentar(4)
escrever(variavel)  # Output: [1, 2, 3, 4]
      </pre>
    </div>

    <div class="code-example">
      <h2>extend - estender</h2>
      <pre>
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.estender(lista2)
escrever(lista1)  # Output: [1, 2, 3, 4, 5, 6]
      </pre>
    </div>

    <div class="code-example">
      <h2>insert - inserir</h2>
      <pre>
variavel = [1, 2, 3]
variavel.inserir(1, 4)
escrever(variavel)  # Output: [1, 4, 2, 3]
      </pre>
    </div>

    <div class="code-example">
      <h2>remove - remover</h2>
      <pre>
variavel = [1, 2, 3, 4]
variavel.remover(2)
escrever(variavel)  # Output: [1, 3, 4]
      </pre>
    </div>

    <div class="code-example">
      <h2>pop - retirar</h2>
      <pre>
variavel = [1, 2, 3]
elemento = variavel.retirar(1)
escrever(variavel)     # Output: [1, 3]
escrever(elemento)  # Output: 2
      </pre>
    </div>

    <div class="code-example">
      <h2>clear - limpar</h2>
      <pre>
variavel = [1, 2, 3]
variavel.limpar()
escrever(variavel)  # Output: []
      </pre>
    </div>

    <div class="code-example">
      <h2>index - indice</h2>
      <pre>
variavel = [1, 2, 3, 4, 3]
indice = variavel.indice(3)
escrever(indice)  # Output: 2
      </pre>
    </div>

    <div class="code-example">
      <h2>count - contar</h2>
      <pre>
variavel = [1, 2, 3, 3, 4]
contagem = variavel.contar(3)
escrever(contagem)  # Output: 2
      </pre>
    </div>

    <div class="code-example">
      <h2>sort - organizar</h2>
      <pre>
variavel = [4, 2, 1, 3]
variavel.organizar()
escrever(variavel)  # Output: [1, 2, 3, 4]
      </pre>
    </div>

    <div class="code-example">
      <h2>reverso - reverter</h2>
      <pre>
variavel = [1, 2, 3]
variavel.reverter()
escrever(variavel)  # Output: [3, 2, 1]
      </pre>
    </div>

    <div class="code-example">
      <h2>copy - copiar</h2>
      <pre>
variavel = [1, 2, 3]
copia_lista = variavel.copia()
escrever(copia_lista)  # Output: [1, 2, 3]
      </pre>
    </div>

  </div>

  <div class="section">
    <h1>Comandos de Caracteres em PortuPy</h1>

    <div class="code-example">
      <h2>capitalize - capitalizar</h2>
      <pre>
texto = "exemplo de texto"
texto_capitalizado = texto.capitalizar()
escrever(texto_capitalizado)  # Output: "Exemplo de texto"
  </pre>
    </div>

    <div class="code-example">
      <h2>lower - minuscula</h2>
      <pre>
texto = "Exemplo de TEXTO"
texto_minuscula = texto.minuscula()
escrever(texto_minuscula)  # Output: "exemplo de texto"
  </pre>
    </div>

    <div class="code-example">
      <h2>upper - maiuscula</h2>
      <pre>
texto = "Exemplo de TEXTO"
texto_maiuscula = texto.maiuscula()
escrever(texto_maiuscula)  # Output: "EXEMPLO DE TEXTO"
  </pre>
    </div>

    <div class="code-example">
      <h2>title - titulo</h2>
      <pre>
texto = "exemplo de texto"
texto_titulo = texto.titulo()
escrever(texto_titulo)  # Output: "Exemplo De Texto"
  </pre>
    </div>

    <div class="code-example">
      <h2>strip - remover_espacos</h2>
      <pre>
texto = "   exemplo   "
texto_sem_espacos = texto.remover_espacos()
escrever(texto_sem_espacos)  # Output: "exemplo"
  </pre>
    </div>

    <div class="code-example">
      <h2>lstrip - lremover_espacos</h2>
      <pre>
texto = "   exemplo   "
texto_sem_espacos_esquerda = texto.lremover_espacos()
escrever(texto_sem_espacos_esquerda)  # Output: "exemplo   "
  </pre>
    </div>

    <div class="code-example">
      <h2>rstrip - rremover_espacos</h2>
      <pre>
texto = "   exemplo   "
texto_sem_espacos_direita = texto.rremover_espacos()
escrever(texto_sem_espacos_direita)  # Output: "   exemplo"
  </pre>
    </div>

    <div class="code-example">
      <h2>replace - substituir</h2>
      <pre>
texto = "exemplo de texto"
novo_texto = texto.substituir("texto", "Python")
escrever(novo_texto)  # Output: "exemplo de Python"
  </pre>
    </div>

    <div class="code-example">
      <h2>split - dividir</h2>
      <pre>
texto = "exemplo de texto"
palavras = texto.dividir()
escrever(palavras)  # Output: ['exemplo', 'de', 'texto']
  </pre>
    </div>

    <div class="code-example">
      <h2>join - juntar</h2>
      <pre>
palavras = ['exemplo', 'de', 'texto']
texto = " ".juntar(palavras)
escrever(texto)  # Output: "exemplo de texto"
  </pre>
    </div>

    <div class="code-example">
      <h2>find - encontrar</h2>
      <pre>
texto = "exemplo de texto"
posicao = texto.encontrar("de")
escrever(posicao)  # Output: 8
  </pre>
    </div>

    <div class="code-example">
      <h2>count - contar</h2>
      <pre>
texto = "exemplo de texto"
contagem = texto.contar("e")
escrever(contagem)  # Output: 3
  </pre>
    </div>

    <div class="code-example">
      <h2>startswith - comeca_com</h2>
      <pre>
texto = "exemplo de texto"
resultado = texto.comeca_com("exemplo")
escrever(resultado)  # Output: Verdadeiro
  </pre>
    </div>

    <div class="code-example">
      <h2>endswith - termina_com</h2>
      <pre>
texto = "exemplo de texto"
resultado = texto.termina_com("texto")
escrever(resultado)  # Output: Verdadeiro
  </pre>
    </div>

    <div class="code-example">
      <h2>isalpha - e_alfabetica</h2>
      <pre>
texto = "exemplo"
resultado = texto.e_alfabetica()
escrever(resultado)  # Output: Verdadeiro
  </pre>
    </div>

    <div class="code-example">
      <h2>isdigit - e_numerica</h2>
      <pre>
texto = "123"
resultado = texto.e_numerica()
escrever(resultado)  # Output: Verdadeiro
  </pre>
    </div>
  </div>



</body>

</html>

</div>


</body>

</html>"""

        # Crie um arquivo HTML temporário
        with open("documentacao.html", "w", encoding="utf-8") as html_file:
            html_file.write(conteudo_html)

        # Abra o arquivo no navegador padrão
        webbrowser.open("documentacao.html")

    def codificarParaPortoPy(self, event=None, *args):
        print('Classe:App - codificarParaPortoPy')
        self.editorPy.text.edit_modified(0)
        codigo = self.editorPy.text.get("1.0", "end-1c")
        resultado = self.decodificador.codificarParaPortoPy(codigo)
        self.controladorEditor = False
        self.editor.text.delete("1.0", "end-1c")
        self.editor.text.insert(END, resultado)

    def codificarParaPython(self, *args):
        print('Classe:App - codificarParaPython')
        self.editor.text.edit_modified(0)
        codigo = self.editor.text.get("1.0", "end-1c")
        resultado = self.decodificador.codificadorParaPython(codigo)
        self.controladorEditor = True
        self.editorPy.text.delete("1.0", "end-1c")
        self.editorPy.text.insert(END, resultado)
        self.editor.remove_underline()
        if not self.arquivoSalvo:
            self.tela.title(f'*PortuPy (beta - V.0.1) - {str(self.arquivo)}* ')
        self.arquivoSalvo = False

    def abrirOpcaoEncontrar(self, event=None):
        print('Classe:App - abrirOpcaoEncontrar')
        self.opcaoEncontrar = False if self.opcaoEncontrar else True
        self.encontrar.exibirTela(self.editor) if self.opcaoEncontrar else self.encontrar.ocultarTela()

    def abrirOpcaoTelaPython(self, event=None):
        print('Classe:App - abrirOpcaoTelaPython')
        self.opcaoTelaPython = False if self.opcaoTelaPython else True
        self.editorPy.exibirTela(self.editor) if self.opcaoTelaPython else self.editorPy.ocultarTela()

    def salvar_em_arquivo(self, event=None):
        print('Classe:App - salvar_em_arquivo')
        conteudo = self.editor.text.get("1.0", "end-1c")

        # Abre uma caixa de diálogo para escolher o nome do arquivo
        if not self.arquivo:
            nome_arquivo = filedialog.asksaveasfilename(
                defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
        else:
            nome_arquivo = self.arquivo

        if nome_arquivo:
            with open(nome_arquivo, "w") as arquivo:
                arquivo.write(conteudo)
            self.arquivo = nome_arquivo
            self.arquivoSalvo = True
            self.tela.title(f'PortuPy (beta - V.0.1) - {str(self.arquivo)}')
        else:
            print("Nenhum arquivo selecionado.")

    def perguntar_salvar(self, event=None):
        print('Classe:App - perguntar_salvar')
        if not self.arquivoSalvo:
            resposta = messagebox.askyesnocancel(
                "Salvar Alterações?", "Deseja salvar as alterações?")
            if resposta is None:
                return
            elif resposta:
                self.salvar_em_arquivo()
            self.abrir_arquivo()
        else:
            self.abrir_arquivo()

    def abrir_arquivo(self):
        print('Classe:App - abrir_arquivo')
        nome_arquivo = filedialog.askopenfilename(
            filetypes=[("Arquivos de Texto", "*.txt")])
        if nome_arquivo:
            self.editor.text.delete("1.0", "end-1c")
            with open(nome_arquivo, "r") as arquivo:
                conteudo = arquivo.read()
                self.editor.text.insert("end", conteudo)
            self.arquivo = nome_arquivo
            self.tela.title(f'PortuPy (beta - V.0.1) - {str(self.arquivo)}')
        self.arquivoSalvo = True

    def fechar_janela(self):
        print('Classe:App - fechar_janela')
        if not self.arquivoSalvo:
            resposta = messagebox.askyesnocancel(
                "Salvar Alterações?", "Deseja salvar as alterações?")
            if resposta is None:
                return
            elif resposta:
                self.salvar_em_arquivo()
            self.tela.destroy()
        else:
            self.tela.destroy()

    def rodarCodigo(self, event=None):
        print('Classe:App - rodarCodigo')
        codigo = self.editor.text.get("1.0", "end-1c")
        resultado = self.decodificador.codificadorParaPython(codigo)
        mensagem = self.run.runCod(resultado)
        if mensagem and mensagem[0] == 'erro':
            if len(mensagem) >= 3:
                self.editor.add_underline(mensagem[2])
            messagebox.showerror('Ops... Algum Problema foi encontrado!', mensagem[1])

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
    tela = App(root)
    tela.exibirTela()
    root.mainloop()
