from random import randint;
from tkinter import  *;
from tkinter import messagebox


choice = int(input('Sua escolha: '))

if choice == 1:
    with open('citacoes.txt', 'r') as ler:
        lista_citacoes = (ler.read()).split(';')

        n = randint(0, (len(lista_citacoes) -1))

        citacao = lista_citacoes[n]
        citacao = citacao.split(' - ')
        autor = citacao[1]
        citacao = citacao[0]
    
        ler.close()

    print(citacao)
    print(autor)


if choice == 2:
    with open('citacoes.txt', 'a') as gravar:
        frase = '"'+ input('Digite a frase aqui: ') + '"'
        autor = input('Digite o nome do autor aqui: ')

        citacao = (f'{frase} - {autor};')
        print(citacao)
        gravar.write(citacao)

        gravar.close()


# Criação da janela pop up
    
# app = Tk()
# app.title('Citação Diaria')

# app.geometry('500x300')

# Label(app, text='Menu').pack()
# # tb_num = Entry(app, txtvariable=)

# # messagebox.showinfo()
# # messagebox.showinfo(title='Citação:', message=lista_citacoes[n])

# app.mainloop()
    
#     # print(lista_citacoes[n])