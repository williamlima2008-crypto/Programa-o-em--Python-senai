import tkinter as tk


janela = tk.Tk()

janela.geometry('500x500')

# texto formulário

tk.Label(janela, text= 'Formulário').pack()

tk.Label(janela, text='nome').pack()

tk.Label(janela, text= 'idade').pack()

tk.Label(janela, text= 'E-mail').pack()

#  input(nome)

nome = tk.Entry(janela,width=30)
nome.pack()

idade = tk.Entry(janela,width=30)
idade.pack()

email = tk.Entry(janela,width=30)
email.pack()




janela.mainloop()
