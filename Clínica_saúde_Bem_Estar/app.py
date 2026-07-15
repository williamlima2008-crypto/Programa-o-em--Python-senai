import sqlite3 # banco de dados
import tkinter as tk # interface 
from tkinter import messagebox # caixas de mensagens
from tkinter import ttk # interface grafica tb
import customtkinter 

def conectar():
    return sqlite3.connect('teste.db')


def criar_tabela():
    conn = conectar()
    c= conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        peso REAL NOT NULL,
        altura REAL NOT NULL,
        imc REAL NOT NULL
        )       
    ''')
    conn.commit()
    conn.close()
  


# CREATE
def inserir_usuario():
    id = entry_id.get()
    nome = entry_nome.get()
    peso = float(entry_peso.get())
    altura =  float(entry_altura.get())
    imc = round(peso / (altura**2),2)
    if nome and peso:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO usuarios(id,nome, peso, altura, imc) VALUES(?,?,?,?,?)', (id, nome, peso, altura, imc))
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'DADOS INSERIDOS COM SUCESSO!') 
        mostrar_usuario()
    else:
        messagebox.showerror('ERRO', 'ALGO DEU ERRADO!') 

# READ
def mostrar_usuario():
    for row in tree.get_children():   
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()    
    c.execute('SELECT * FROM usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert("", "end", values=(usuario[0], usuario[1],usuario[2],usuario[3], usuario[4]))
    conn.close()    


# DELETE
def delete_usuario():
    dado_del = tree.selection()
    if dado_del:
       user_id = tree.item(dado_del)['values'][0]
       conn = conectar()
       c = conn.cursor()    
       c.execute('DELETE FROM usuarios WHERE id = ? ',(user_id,))
       conn.commit()
       conn.close()
       messagebox.showinfo('', 'DADO DELETADO')
       mostrar_usuario()

    else:
       messagebox.showerror('', 'OCORREU UM ERRO')  

# UPDATE 
       
def editar():
     selecao = tree.selection()
     if selecao:
         user_id = tree.item(selecao)['values'][0]
         novo_nome = entry_nome.get()
         novo_peso = float(entry_peso.get())
         novo_altura = float(entry_altura.get())
         novo_imc = round(novo_peso/(novo_altura**2),2)

         if novo_nome :
            conn = conectar()
            c = conn.cursor()    
            c.execute('UPDATE usuarios SET nome = ? , peso = ?, altura = ?, imc = ? WHERE id = ? ',(novo_nome,novo_peso,novo_altura, novo_imc,user_id))
            conn.commit()
            conn.close()  
            messagebox.showinfo('', 'DADOS ATUALIZADOS')
            mostrar_usuario()

         else:
             messagebox.showwarning('', 'PREENCHA TODOS OS CAMPOS')

     else:
            messagebox.showerror('','ALGO DEU ERRADO!')


janela = tk.Tk()
janela.title('CRUD')

label_nome = tk.Label(janela, text='Nome:')
label_nome.grid(row=0, column=0, padx=10, pady=10)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_peso = tk.Label(janela, text = 'Peso:')
label_peso.grid(row=1, column=0, padx=10, pady=10)

entry_peso = tk.Entry(janela, text = 'Peso:')
entry_peso.grid(row=1, column=1, padx=10, pady=10)



label_altura = tk.Label(janela, text = 'Altura:')
label_altura.grid(row=2, column=0, padx=10, pady=10)

entry_altura = tk.Entry(janela, text = 'Altura:')
entry_altura.grid(row=2, column=1, padx=10, pady=10)


# label_imc = tk.Label(janela, text = 'IMC:')
# label_imc.grid(row=3, column=0, padx=10, pady=10)

# entry_imc = tk.Entry(janela, text = 'IMC:')
# entry_imc.grid(row=3, column=1, padx=10, pady=10)


label_id = tk.Label(janela, text = 'ID:')
label_id.grid(row=4, column=0, padx=10, pady=10)

entry_id = customtkinter.CTkEntry(janela)
entry_id.grid(row=4, column=1, padx=10, pady=10)


btn_salvar = tk.Button(janela, text='Salvar', command=inserir_usuario)
btn_salvar.grid(row=5, column=0, padx=10, pady=10)

btn_deletar = tk.Button(janela, text='deletar', command=delete_usuario )
btn_deletar.grid(row=6, column=0, padx=10, pady=10)

btn_atualizar = tk.Button(janela, text='atualizar', command=editar)
btn_atualizar.grid(row=7, column=0, padx=10, pady=10)



columns = ('ID', 'NOME', 'PESO', 'ALTURA', 'IMC')
tree = ttk.Treeview(janela, columns=columns, show='headings')
tree.grid(row=8,column=0,columnspan=2,padx=10, pady=10)


for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_usuario()


janela.mainloop()
