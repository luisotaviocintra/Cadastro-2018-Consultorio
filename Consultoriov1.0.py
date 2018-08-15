# -*- coding: iso-8859-1 -*-

import sqlite3
from tkinter import *
from tkinter import messagebox

# Criar conexÃ£o e cursor
con = sqlite3.connect('paciente.db')
cur = con.cursor()



# Criar tabela clientes
cur.execute("CREATE TABLE IF NOT EXISTS paciente ("
            "codigo INTEGER PRIMARY KEY,"
            "nome TEXT,"
            "endereco TEXT,"
            "telefone TEXT,"
            "convenio TEXT"
            "datanascimento TEXT"
            "cpf TEXT"
            "observacao TEXT)")

class main:

    def __init__(self, master):

        # --------------------------------------TKINTER INTERFACE------------------------------------------------#
        self.frame1 = Frame(master, bg='sky blue')
        self.frame1.configure(relief=GROOVE)
        self.frame1.configure(borderwidth="2")
        self.frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.51)

        #--------------------------Titulo--------------------------#
        Label(self.frame1, text='CADASTRO', font=('Ariel', '30'), bg='sky blue').place(relx=0.30, rely=0.01)


        # --------------------------Campo Entrada Nome--------------------------#
        self.txtCodigo = StringVar()
        self.lblcodigo = Label(master, text="Código")
        self.lblcodigo.place(relx=0.01, rely=0.10, relheight=0.03, relwidth=0.10)
        self.entCodigo = Entry(master, textvariable=self.txtCodigo)
        self.entCodigo.place(relx=0.12, rely=0.10)

        self.txtNome = StringVar()
        self.lblnome = Label(master, text="Nome")
        self.lblnome.place(relx=0.01, rely=0.14, relheight=0.03, relwidth=0.10)
        self.entNome = Entry(master, textvariable=self.txtNome)
        self.entNome.place(relx=0.12, rely=0.14)

        self.txtEndereco = StringVar()
        self.lblendereco = Label(master, text="Endereço")
        self.lblendereco.place(relx=0.01, rely=0.18, relheight=0.03, relwidth=0.10)
        self.entEndereco = Entry(master, textvariable=self.txtEndereco)
        self.entEndereco.place(relx=0.12, rely=0.18)

        self.txtTelefone = StringVar()
        self.lbltelefone = Label(master, text="Telefone")
        self.lbltelefone.place(relx=0.01, rely=0.22, relheight=0.03, relwidth=0.10)
        self.entTelefone = Entry(master, textvariable=self.txtTelefone)
        self.entTelefone.place(relx=0.12, rely=0.22)

        self.txtConvenio = StringVar()
        self.lblconvenio = Label(master, text="Convenio")
        self.lblconvenio.place(relx=0.01, rely=0.26, relheight=0.03, relwidth=0.10)
        self.entConvenio = Entry(master, textvariable=self.txtConvenio)
        self.entConvenio.place(relx=0.12, rely=0.26)

        self.txtDatanascimento = StringVar()
        self.lbldatanascimento = Label(master, text="Data de Nascimento")
        self.lbldatanascimento.place(relx=0.01, rely=0.30, relheight=0.03, relwidth=0.10)
        self.entDatanascimento = Entry(master, textvariable=self.txtDatanascimento)
        self.entDatanascimento.place(relx=0.12, rely=0.30)

        self.txtCPF = StringVar()
        self.lblcpf = Label(master, text="CPF")
        self.lblcpf.place(relx=0.01, rely=0.34, relheight=0.03, relwidth=0.10)
        self.entCPF = Entry(master, textvariable=self.txtCPF)
        self.entCPF.place(relx=0.12, rely=0.34)

        self.txtObservacao = StringVar()
        self.lblobservacao = Label(master, text="Observação")
        self.lblobservacao.place(relx=0.01, rely=0.38, relheight=0.03, relwidth=0.10)
        self.entObservacao = Entry(master, textvariable=self.txtObservacao)
        self.entObservacao.place(relx=0.12, rely=0.38)

        self.listPacientes = Listbox(master, bg='red')
        self.listPacientes.place(relx=0.51, rely=0, relheight=1, relwidth=1.10)

        scrollPacientes = Scrollbar(master)
        scrollPacientes.place(relx=0.99, rely=0, relheight=1, relwidth=0.01)

        #----- Botões ---#

        self.btnInserir = Button(master, text="Inserir", command= self.cadastraclientes)
        self.btnInserir.place(relx=0.01, rely=0.45, relheight=0.04, relwidth=0.06)

        self.btnVerTodos = Button(master, text="Ver Todos")
        self.btnVerTodos.place(relx=0.01, rely=0.51, relheight=0.04, relwidth=0.06)

        self.btnBuscar = Button(master, text="Buscar")
        self.btnBuscar.place(relx=0.01, rely=0.57, relheight=0.04, relwidth=0.06)

        self.btnAtualizar = Button(master, text="Atualizar")
        self.btnAtualizar.place(relx=0.01, rely=0.63, relheight=0.04, relwidth=0.06)

        self.btnDelete = Button(master, text="Deletar")
        self.btnDelete.place(relx=0.01, rely=0.69, relheight=0.04, relwidth=0.06)

        self.btnFechar = Button(master, text="Fechar")
        self.btnFechar.place(relx=0.01, rely=0.75, relheight=0.04, relwidth=0.06)

    def cadastraclientes(self):
        codigo = self.txtCodigo.get()
        nome = self.txtNome.get()
        endereco = self.txtEndereco.get()
        telefone = self.txtTelefone.get()
        convenio = self.txtConvenio.get()
        datanascimento = self.txtDatanascimento.get()
        cpf = self.txtCPF.get()
        observacao = self.txtObservacao.get()
        try:
            cur.execute("INSERT INTO paciente VALUES(?,?,?,?,?,?,?,?)",
                        (codigo, nome, endereco, telefone, convenio, datanascimento, cpf, observacao))
        except:
            messagebox.showinfo('Aviso!', 'Código já cadastrado')
        con.commit()
        self.txtCodigo.delete(0, END)



root = Tk()
root.title("Cadastro_C")
root.geometry("1366x768")
main(root)
root.mainloop()