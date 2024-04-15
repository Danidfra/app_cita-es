from random import randint
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def mensagem():
    with open('citacoes.txt', 'r') as ler:
        lista_citacoes = (ler.read()).split(';')

        n = randint(0, (len(lista_citacoes) - 1))

        citacao = lista_citacoes[n]
        citacao = citacao.split(' - ')
        autor = citacao[1]
        frase = citacao[0]

        citacao = f'{frase}\n\n{autor}'

        ler.close()
    
    # Criação da janela pop up
    janela_citacao = Toplevel()
    janela_citacao.title('Citação Diária')

    # Carregando a imagem
    imagem = PhotoImage(file='quote.png')  # Altere 'sua_imagem.png' para o nome da sua imagem
    label_imagem = Label(janela_citacao, image=imagem)
    label_imagem.pack()

    # Adicionando a citação
    label_citacao = Label(janela_citacao, text=citacao)
    label_citacao.pack()

    janela_citacao.mainloop()

# Criação da janela principal
menu = Tk()
menu.title('Citação Diaria')
menu.iconbitmap('quote.png')

# Forçar atualização do cache do Tkinter
menu.update_idletasks()

# Definição da geometria
largura = 300
altura = 300
largura_screen = menu.winfo_screenwidth()
altura_screen = menu.winfo_screenheight()
posx = int(largura_screen / 2 - largura / 2)
posy = int(altura_screen / 2 - altura / 2)
menu.geometry(f'{largura}x{altura}+{posx}+{posy}')

# Criando a interface
caixa = ttk.Frame(menu, padding=10)
caixa.grid()
ttk.Label(caixa, text='Clique em show para ver a citação do dia').grid(column=0, row=1, sticky='nsew')
ttk.Button(caixa, text='Show', command=mensagem).grid(column=0, row=2, sticky='nsew')

menu.mainloop()
