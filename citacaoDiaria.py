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
    imagem = PhotoImage(file='assets/quote.png')
    label_imagem = Label(janela_citacao, image=imagem)
    label_imagem.pack()


    # Adicionando a citação
    label_citacao = Label(janela_citacao, text=citacao)
    label_citacao.pack()

    # Adicionando botão 'i got it'
    botao = Button(janela_citacao, text='I got it', command=lambda: clique_do_botao(janela_citacao))
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
    label_imagem.pack(side='top', pady=20)

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
    print('teste')
    janela_citacoes = Toplevel()
    janela_citacoes.title('Citações')

    pos_x, pos_y= posXY()
    janela_citacoes.geometry(f'+{pos_x}+{pos_y}')


    # Adicionando icone
    imagem = PhotoImage(file='assets/quote.png')
    label_imagem = Label(janela_citacoes, image=imagem)
    label_imagem.pack()

    with open('citacoes.txt', 'r') as ler:
        lista_citacoes = (ler.read()).split(';')

        citacao = ''

        for i in lista_citacoes:
            if i == '':
                  continue

            citacao = citacao + i + '\n' 


        ler.close()
    
    label_citacao = Label(janela_citacoes, text='teste')
    label_citacao.pack()





# Criação da janela principal
menu = Tk()
menu.title('Citação Diaria')
menu.iconbitmap('assets/quote.ico')

# Forçar atualização do cache do Tkinter
menu.update_idletasks()

# Definição da geometria
pos_x, pos_y= posXY()
menu.geometry(f'+{pos_x}+{pos_y}')

# Criando a interface para centralizar
caixa = ttk.Frame(menu, padding=40)
caixa.grid(sticky='nsew')

# Criando a interface
ttk.Label(caixa, text='Clique em uma das opções abaixo: ').grid(column=0, row=1, sticky='nsew')
ttk.Button(caixa, text='1 - Take one', command=mensagem).grid(column=0, row=2, sticky='nsew')
ttk.Button(caixa, text='2 - Add one', command=adicionarCit).grid(column=0, row=3, sticky='nsew')
ttk.Button(caixa, text='3 - Show all', command=mostrarTodas).grid(column=0, row=4, sticky='nsew')


menu.mainloop()




# from random import randint;
# from tkinter import *
# from tkinter import messagebox
# from tkinter import ttk

# def mensagem():
#     with open('citacoes.txt', 'r') as ler:
#         lista_citacoes = (ler.read()).split(';')

#         n = randint(0, (len(lista_citacoes) -1))

#         citacao = lista_citacoes[n]
#         citacao = citacao.split(' - ')
#         autor = citacao[1]
#         frase = citacao[0]

#         citacao = f'{frase}\n\n{autor}'

#         ler.close()
    
#     m = messagebox.showinfo(title='Citação:', message=citacao, _icon='quote.ico')
#     return m 

# # choice = int(input('Sua escolha: '))

# # if choice == 1:
   

# #     print(citacao)
# #     print(autor)


# # if choice == 2:
# #     with open('citacoes.txt', 'a') as gravar:
# #         frase = '"'+ input('Digite a frase aqui: ') + '"'
# #         autor = input('Digite o nome do autor aqui: ')

# #         citacao = (f'{frase} - {autor};')
# #         print(citacao)
# #         gravar.write(citacao)

# #         gravar.close()


# # Criação da janela pop up
    
# menu = Tk()
# menu.title('Citação Diaria')
# menu.iconbitmap('assets/quote.ico')

# # resolução da caixa
# largura = 400
# altura = 400

# # resoluçao do sistema
# largura_screen = menu.winfo_screenwidth()
# altura_screen = menu.winfo_screenheight()

# # calculando a posição
# posx = int(largura_screen/2 - largura/2)
# posy = int(altura_screen/2 - altura/2)

# #  definindo a geometry
# menu.geometry(f'{largura}x{altura}+{posx}+{posy}')


# caixa = ttk.Frame(menu, padding=10)
# caixa.grid()
# ttk.Label(caixa, text='Menu').grid(column=1, row=1)



# ttk.Button(caixa, text='Show', command=mensagem,).grid(column=1, row=2)





# # tb_num = Entry(menu, txtvariable=)

# # messagebox.showinfo()

    
# menu.mainloop()
#     # print(lista_citacoes[n])