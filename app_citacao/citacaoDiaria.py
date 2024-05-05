from random import randint
from tkinter import *
from tkinter import ttk
   

def posXY():

    largura = menu.winfo_reqwidth()
    altura = menu.winfo_reqheight()
    largura_screen = menu.winfo_screenwidth()
    altura_screen = menu.winfo_screenheight()
    posx = int(largura_screen / 2 - largura / 2)
    posy = int(altura_screen / 2 - altura / 2)

    return posx, posy

def clique_do_botao(janela):
    janela.destroy()

def gravarCit(janela, vec, vea):

    citacao = vec.get()
    autor = vea.get()

    with open('citacoes.txt', 'a') as gravar:

        citacao = (f'"{citacao}" - {autor};')
        print(citacao)
        gravar.write(citacao)

        gravar.close()
    
    janela.destroy()

def salvarEdit(janela, texto):

    caracteres = list(texto)

    # Lista para armazenar os caracteres sem '\n'
    caracteres_sem_n = []

    # Variável para acompanhar se o caractere anterior foi '\n'
    caractere_anterior_n = False

    # Percorrendo a lista de caracteres
    for char in caracteres:
        # Verificando se o caractere atual é '\n' e o anterior também foi '\n'
        if char == '\n' and caractere_anterior_n:
            # Se ambos forem '\n', não adicionamos ';' à lista
            continue
        # Adicionando o caractere à lista caracteres_sem_n
        caracteres_sem_n.append(char)
        # Atualizando o valor de caractere_anterior_n
        caractere_anterior_n = (char == '\n')

    # Substituindo todas as ocorrências de dois '\n' por um ';'
    caracteres_sem_n = [char if char != '\n' else ';' for char in caracteres_sem_n]
    citacoes = caracteres_sem_n
    citacoes = ''.join(citacoes)

    with open('citacoes.txt', 'w') as gravar:
            gravar.write(citacoes)



    janela.destroy()

def mensagem():
    with open('citacoes.txt', 'r') as ler:
        lista_citacoes = (ler.read()).split(';')

        n = randint(0, (len(lista_citacoes) - 1))

        citacao = lista_citacoes[n]
        citacao = citacao.split(' - ')

        try:
            autor = citacao[1]
        except IndexError:
            print(citacao)
        frase = citacao[0]

        citacao = f'{frase}\n\n{autor}'

        ler.close()
    
    # Criação da janela pop up
    janela_citacao = Toplevel()
    janela_citacao.title('Citação Diária')

    # Container pai
    caixa = ttk.Frame(janela_citacao, padding=20)
    caixa.pack(expand=True)

    # Carregando a imagem
    imagem = PhotoImage(file='assets/quote.png')
    label_imagem = Label(caixa, image=imagem)
    label_imagem.pack(side='top', pady=10)


    # Adicionando a citação
    label_citacao = Label(caixa, text=citacao)
    label_citacao.pack()

    # Adicionando botão 'i got it'
    botao = Button(caixa, text='I got it', command=lambda: clique_do_botao(janela_citacao))
    botao.pack()

    # Atribuindo os retornos da função posXY
    pos_x, pos_y= posXY()

    # Definindo geometria da janela
    janela_citacao.geometry(f'+{pos_x}+{pos_y}')


    janela_citacao.mainloop()

def adicionarCit():
    janela_add_citacao = Toplevel()
    janela_add_citacao.title('Adicionando nova citação')

    # Posicionando janela no centro 
    pos_x, pos_y= posXY()
    janela_add_citacao.geometry(f'+{pos_x}+{pos_y}')

    # 
    caixa_2 = ttk.Frame(janela_add_citacao, padding=40)
    caixa_2.pack(expand=True)

    # Adicionando uma imagem a janela
    imagem = PhotoImage(file='assets/quote.png')
    label_imagem = Label(caixa_2, image=imagem)
    label_imagem.pack(side='top', pady=10)

    # Criando variaveis para armazenar os valores das 'entrys'
    valor_entry_citacao = StringVar()
    valor_entry_autor = StringVar()

    # Criando duas entradas de dados
    label_citacao = ttk.Label(caixa_2, text='Digite abaixo a citação:')
    label_citacao.pack(anchor='w')
    entry_citacao = ttk.Entry(caixa_2, textvariable=valor_entry_citacao)
    entry_citacao.pack()

    label_citacao_2 = ttk.Label(caixa_2, text='Digite abaixo o autor:')
    label_citacao_2.pack(anchor='w')
    entry_autor = ttk.Entry(caixa_2, textvariable=valor_entry_autor)
    entry_autor.pack()


    ttk.Button(caixa_2, text='Enviar', command=lambda: gravarCit(janela_add_citacao, valor_entry_citacao, valor_entry_autor)).pack(pady=20)
    # ttk.Button(caixa_2, text='Enviar', command=lambda: gravarCit(janela_add_citacao, valor_entry_citacao, valor_entry_autor)).grid(row=2, column=0)



    janela_add_citacao.mainloop()

def mostrarTodas():

    with open('citacoes.txt', 'r') as ler:
        lista_citacoes = (ler.read()).split(';')

        citacao = ''

        for i in lista_citacoes:
            for j in i:

                if i == '':
                    continue

            citacao = citacao + i + '\n\n' 


        ler.close()

    janela_citacoes = Toplevel()
    janela_citacoes.title('Citações')

    # Criando container
    caixa = ttk.Frame(janela_citacoes, padding=20)
    caixa.pack(expand=True)

    # Adicionando icone
    imagem = PhotoImage(file='assets/quote.png')
    label_imagem = Label(caixa, image=imagem)
    label_imagem.image = imagem
    label_imagem.pack(side='top', pady=5)

    # Adiciona label
    label_text = Label(caixa, text='Segue abaixo todas as citações:')
    label_text.pack(pady=10)
        

    # Criando caixa para mostrar as citações
    text_area = Text(caixa, wrap="word" ,borderwidth=20, state="disabled")
    text_area.pack(side="left", fill="both", expand=True)

    # Inserindo as citações
    text_area.config(state="normal")
    text_area.insert("1.0", citacao)
    text_area.config(state="disabled")

    # Adicionar barra de rolagem lateral
    scroll_bar = Scrollbar(caixa, command=text_area.yview)
    scroll_bar.pack(side="right", fill="y")
    text_area.config(yscrollcommand=scroll_bar.set)
    
    # Posicionando a janela
    pos_x, pos_y= posXY()
    janela_citacoes.geometry(f'+{pos_x}+{pos_y}')

def editarCit():

    with open('citacoes.txt', 'r') as ler:
        lista_citacoes = (ler.read()).split(';')

        citacao = ''

        for i in lista_citacoes:
            for j in i:

                if i == '':
                    continue

            citacao = citacao + i + '\n\n' 


        ler.close()

    janela = Toplevel()
    janela.title('Citações')

    # Criando container
    caixa = ttk.Frame(janela, padding=20)
    caixa.pack(expand=True)

    # Adicionando icone
    imagem = PhotoImage(file='assets/quote.png')
    label_imagem = Label(caixa, image=imagem)
    label_imagem.image = imagem
    label_imagem.pack(side='top', pady=10)

    # Adiciona label
    label_text = Label(caixa, text='Segue abaixo todas as citações:')
    label_text.pack(pady=5)

    # Container
    container_citacoes = ttk.Frame(caixa, padding=10)
    container_citacoes.pack()


    


    # Criando caixa para mostrar as citações
    text_area = Text(container_citacoes, wrap="word" ,borderwidth=20)
    text_area.pack(side="left", fill="both", expand=True)

    # Inserindo as citações
    text_area.insert("1.0", citacao)

    # Adicionar barra de rolagem lateral
    scroll_bar = Scrollbar(container_citacoes, command=text_area.yview)
    scroll_bar.pack(side="right", fill="y")
    text_area.config(yscrollcommand=scroll_bar.set)
    
    getTexto = lambda: text_area.get('1.0', 'end')

    # Adicionando botão
    botao_enviar = ttk.Button(caixa, text='Salvar edições', command=lambda: salvarEdit(janela, getTexto()), width=10).pack(side='bottom')

    # Posicionando a janela
    pos_x, pos_y= posXY()
    janela.geometry(f'+{pos_x}+{pos_y}')


# Criação da janela principal
menu = Tk()
menu.title('Citação Diaria')
# menu.iconbitmap('assets/quote.ico')

# Forçar atualização do cache do Tkinter
menu.update_idletasks()

# Definição da geometria
pos_x, pos_y= posXY()
menu.geometry(f'+{pos_x}+{pos_y}')

# Criando a interface para centralizar
caixa = ttk.Frame(menu, padding=40)
caixa.pack(expand=True)

# Adicionando imagem ao menu inicial
imagem = PhotoImage(file='assets/quote.png')
label_imagem = Label(caixa, image=imagem)
label_imagem.image = imagem
label_imagem.pack(side='top', pady=10)

# Criando a interface
ttk.Label(caixa, text='Escolha uma das opções abaixo:').pack()
ttk.Button(caixa, text='1 - Take one', command=mensagem, width=10).pack()
ttk.Button(caixa, text='2 - Add one', command=adicionarCit, width=10).pack()
ttk.Button(caixa, text='3 - Show all', command=mostrarTodas, width=10).pack()
ttk.Button(caixa, text='4 - Edit all', command=editarCit, width=10).pack()

menu.mainloop()