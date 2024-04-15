from random import randint;
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def mensagem():
    with open('citacoes.txt', 'r') as ler:
        lista_citacoes = (ler.read()).split(';')

        n = randint(0, (len(lista_citacoes) -1))

        citacao = lista_citacoes[n]
        citacao = citacao.split(' - ')
        autor = citacao[1]
        frase = citacao[0]

        citacao = f'{frase}\n\n{autor}'

        ler.close()
    
    m = messagebox.showinfo(title='Citação:', message=citacao, _icon='quote.ico')
    return m 

# choice = int(input('Sua escolha: '))

# if choice == 1:
   

#     print(citacao)
#     print(autor)


# if choice == 2:
#     with open('citacoes.txt', 'a') as gravar:
#         frase = '"'+ input('Digite a frase aqui: ') + '"'
#         autor = input('Digite o nome do autor aqui: ')

#         citacao = (f'{frase} - {autor};')
#         print(citacao)
#         gravar.write(citacao)

#         gravar.close()


# Criação da janela pop up
    
menu = Tk()
menu.title('Citação Diaria')
menu.iconbitmap('assets/quote.ico')

# resolução da caixa
largura = 400
altura = 400

# resoluçao do sistema
largura_screen = menu.winfo_screenwidth()
altura_screen = menu.winfo_screenheight()

# calculando a posição
posx = int(largura_screen/2 - largura/2)
posy = int(altura_screen/2 - altura/2)

#  definindo a geometry
menu.geometry(f'{largura}x{altura}+{posx}+{posy}')


caixa = ttk.Frame(menu, padding=10)
caixa.grid()
ttk.Label(caixa, text='Menu').grid(column=1, row=1)



ttk.Button(caixa, text='Show', command=mensagem,).grid(column=1, row=2)





# tb_num = Entry(menu, txtvariable=)

# messagebox.showinfo()

    
menu.mainloop()
    # print(lista_citacoes[n])