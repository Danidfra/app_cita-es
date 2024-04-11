from random import randint;
from tkinter import  *;
from tkinter import messagebox

with open('citacoes.txt', 'r') as ler:
    lista_citacoes = (ler.read()).split(';')

    n = randint(0, (len(lista_citacoes) -1))


app = Tk()
app.title('Citação Diaria')

app.geometry('500x300')

Label(app, text='Menu').pack()
# tb_num = Entry(app, txtvariable=)

# messagebox.showinfo()
# messagebox.showinfo(title='Citação:', message=lista_citacoes[n])

app.mainloop()
    
    # print(lista_citacoes[n])