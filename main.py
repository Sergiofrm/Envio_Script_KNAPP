
# Projeto : Envio de Script
# Autores : Sérgio Felipe Ribeiro De Melo

from ast import Delete
from cgitb import text
from contextvars import copy_context
from email import message
import shutil
from smtplib import quotedata
from telnetlib import STATUS
from tkinter import *
from tkinter import messagebox
from turtle import right, title, width
from unittest import result
from xml.dom import ValidationErr


class Application():

    def __init__(self, master=None):

        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 20
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 15
        self.container2.pack()

# Espaçamento do Botão Inserir

        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 10
        self.container6.pack()

#########################################################

        self.container3 = Frame(master)
        self.container3["padx"] = 25
        self.container3["pady"] = 15
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 40
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container8 = Frame(master)
        self.container8["padx"] = 25
        self.container8["pady"] = 25
        self.container8.pack()

# Espaçamento do Excluir
        self.container7 = Frame(master)
        self.container7["padx"] = 10
        self.container7["pady"] = 10
        self.container7.pack()

        self.titulo = Label(self.container1, text="Envio de Script - OPENBOX ")
        self.titulo["font"] = ("Segoe UI", "10", "bold")
        self.titulo.pack()

        self.container9 = Frame(master)
        self.container9["padx"] = 15
        self.container9["pady"] = 20
        self.container9.pack()

# Parte do botão - Inserir e Excluir - Botão2
        self.container19 = Frame(master)
        self.container19["padx"] = 5
        self.container19["pady"] = 10
        self.container19.pack()

        self.container20 = Frame(master)
        self.container20["padx"] = 15
        self.container20["pady"] = 20
        self.container20.pack()

# Parte do botão - Adicionar + Materias

        self.container21 = Frame(master)
        self.container21["padx"] = 15
        self.container21["pady"] = 1
        self.container21.pack()

        self.container51 = Frame(master)
        self.container51["padx"] = 45
        self.container51["pady"] = 105
        self.container51.pack(side=RIGHT)

# Botões - Primeira Parte

        self.btnInserir = Button(
            self.container6, text="Inserir", font=self.fonte, width=10)
        self.btnInserir["command"] = self.inserir
        self.btnInserir.pack(side=LEFT)

        self.btnExcluir = Button(
            self.container6, text="Excluir", font=self.fonte, width=10)
        self.btnExcluir["command"] = self.excluir
        self.btnExcluir.pack(side=LEFT)

# Botões - Primeira Parte 2

        self.btnInserir2 = Button(
            self.container19, text="Inserir", font=self.fonte, width=10)
        self.btnInserir2["command"] = self.inserir_2
        self.btnInserir2.pack(side=LEFT)

        self.btnExcluir2 = Button(
            self.container19, text="Excluir", font=self.fonte, width=10)
        self.btnExcluir2["command"] = self.excluir_2
        self.btnExcluir2.pack(side=LEFT)

        self.btnadd = Button(
            self.container21, text="+", font=self.fonte, width=3)
        self.btnadd["command"] = self.add
        self.btnadd.pack(side=RIGHT)


# - Validação do Script

        self.txtean14 = Entry(self.container8)
        self.txtean14["width"] = 150
        self.txtean14["font"] = self.fonte
        self.txtean14.pack(side=LEFT)
        self.txtean14

# Campo de Material

        self.subtitulo = Label(
            self.container9, text="----------------------------------------  Envio de Script - PICKING  ---------------------------------------- ")
        self.subtitulo["font"] = ("Segoe UI", "10", "bold")
        self.subtitulo.pack(side=RIGHT)

        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 30
        self.container10.pack()

        self.container11 = Frame(master)
        self.container11["padx"] = 80
        self.container11["pady"] = 5
        self.container11.pack()


# - Validação do EAN-13 - CX - PARTE 1

        self.lblean13 = Label(
            self.container3, text="Digitar - EAN13", font=self.fonte, width=15)
        self.lblean13.pack(side=LEFT)

        self.txtean13 = Entry(self.container3)

        self.txtean13["width"] = 30
        self.txtean13["font"] = self.fonte
        self.txtean13.pack(side=LEFT)


# - Validação da CX SEPARAÇÃO - PARTE 1

        self.lblcxseparacao = Label(
            self.container4, text="Digitar -CXSEP", font=self.fonte, width=15)
        self.lblcxseparacao.pack(side=LEFT)
        self.txtcxseparacao = Entry(
            self.container4, validate='key')

        self.txtcxseparacao["width"] = 30
        self.txtcxseparacao["font"] = self.fonte

        self.txtcxseparacao.pack(side=LEFT)


# - Validação do EAN-13 - CX - PARTE 2

        self.lbcx = Label(
            self.container20, text="Digitar - EAN13", font=self.fonte, width=15)
        self.lbcx.pack(side=LEFT)

        self.txtcx = Entry(self.container20)

        self.txtcx["width"] = 30
        self.txtcx["font"] = self.fonte
        self.txtcx.pack(side=LEFT)


# - Validação da CX SEPARAÇÃO - PARTE 2

        self.lblsep = Label(
            self.container20, text="Digitar -CXSEP", font=self.fonte, width=15)
        self.lblsep.pack(side=LEFT)
        self.txtsep = Entry(
            self.container20, validate='key')

        self.txtsep["width"] = 30
        self.txtsep["font"] = self.fonte

        self.txtsep.pack(side=LEFT)

# - Material

        self.lblean13 = Label(
            self.container10, text="Material", font=self.fonte, width=20)
        self.lblean13.pack(side=LEFT)

        self.material = Entry(self.container10)

        self.material["width"] = 15
        self.material["font"] = self.fonte
        self.material.pack(side=LEFT)

# - Quantidade

        self.lblean13 = Label(
            self.container10, text="Quantidade", font=self.fonte, width=20)
        self.lblean13.pack(side=LEFT)

        self.quantidade = Entry(self.container10)

        self.quantidade["width"] = 10
        self.quantidade["font"] = self.fonte
        self.quantidade.pack(side=LEFT)

# - Status

        self.lblean13 = Label(
            self.container10, text="Status", font=self.fonte, width=20)
        self.lblean13.pack(side=LEFT)

        self.status = Entry(self.container10)

        self.status["width"] = 5
        self.status["font"] = self.fonte
        self.status.pack(side=LEFT)

# - Posição 01

        self.lblean13 = Label(
            self.container10, text="Posição_01", font=self.fonte, width=20)
        self.lblean13.pack(side=LEFT)

        self.posi1 = Entry(self.container10)

        self.posi1["width"] = 5
        self.posi1["font"] = self.fonte
        self.posi1.pack(side=LEFT)

# - Posição 02

        self.lblean13 = Label(
            self.container10, text="Posição_02", font=self.fonte, width=20)
        self.lblean13.pack(side=LEFT)

        self.posi2 = Entry(self.container10)

        self.posi2["width"] = 5
        self.posi2["font"] = self.fonte
        self.posi2.pack(side=LEFT)

# - Validação do Script 2

        self.txtean15 = Entry(self.container11)
        self.txtean15["width"] = 150
        self.txtean15["font"] = self.fonte
        self.txtean15.pack(side=LEFT)
        self.txtean15

    def add(self):
        sep2 = self.txtcx.get()
        cxp2 = self.txtsep.get()
        material = self.material.get()
        quantidade = self.quantidade.get()
        status = self.status.get()
        posi1 = self.posi1.get()
        posi2 = self.posi2.get()
        txt4 = '            '
        # 'material'
        #'            '
        # 'quntd,status,pos1,pos2'

        if (sep2 != "" and cxp2 != "") and (material != "" and quantidade != "" and status != "" and posi1 != "" and posi2 != ""):
            # Adicionar Elementos

            self.txtean15.insert(END, material+txt4 +
                                 quantidade+status+posi1+posi2)

            # Depois Apagar

            self.material.delete(0, END)
            self.quantidade.delete(0, END)
            self.status.delete(0, END)
            self.posi1.delete(0, END)
            self.posi2.delete(0, END)
        else:
            messagebox.showwarning(
                "Se Liga !!!", "Favor Preencher os Campos dos materias")

    def inserir_2(self):

        sep2 = self.txtcx.get()
        cxp2 = self.txtsep.get()
        material = self.material.get()
        quantidade = self.quantidade.get()
        status = self.status.get()
        posi1 = self.posi1.get()
        posi2 = self.posi2.get()
        txt1 = '1234532R1004'
        # 'ean13''ean1-3'
        txt2 = '0001D10'
        # 'cx'
        txt3 = '  T0306010011509101X0551804020303'
        # 'material'
        txt4 = '            '
        # 'quntd,status,pos1,pos2'
        # 'material'
        #'            '
        # 'quntd,status,pos1,pos2'
        # 'material'
        #'            '
        # 'quntd,status,pos1,pos2'
        if cxp2 != "" and sep2 != "":
            self.txtean15.insert(END, txt1+sep2+txt2+cxp2 +
                                 txt3+material+txt4+quantidade+status+posi1+posi2)
            self.material.delete(0, END)
            self.quantidade.delete(0, END)
            self.status.delete(0, END)
            self.posi1.delete(0, END)
            self.posi2.delete(0, END)
            self.material.focus_force()

        else:
            messagebox.showwarning(
                "AVISO!!!", "Favor preencher o campo de EAN-13 ou CX-SEP")

    def inserir(self):

        cx = self.txtean13.get()
        sep = self.txtcxseparacao.get()
        txt = '0005632R1004'
        txt2 = '0001D10'
        text_espa = "  "
        text_final = 'T0306010011430001'

        if cx != "" and sep != "":
            self.txtean14.insert(END, txt+cx+txt2+sep+text_espa+text_final)

        else:
            messagebox.showwarning(
                "SE LIGA !!! ", "Favor preencher a Caixa de Separação e Caixa Ficticia")

    def excluir_2(self):
        self.txtean15.delete(0, END)
        self.txtcx.delete(0, END)
        self.txtsep.delete(0, END)
        self.material.delete(0, END)
        self.quantidade.delete(0, END)
        self.status.delete(0, END)
        self.posi1.delete(0, END)
        self.posi2.delete(0, END)
        messagebox.showwarning("JS - Solutions ", "Excluido com Sucesso!!")
        self.txtcx.focus_force()

    def excluir(self):
        self.txtean14.delete(0, END)
        self.txtean13.delete(0, END)
        self.txtcxseparacao.delete(0, END)
        messagebox.showwarning("JS - Solutions ", "Excluido com Sucesso!!")
        self.txtean13.focus_force()


root = Tk()
root.title("Projeto - KNAPP")

Application(root)
root.mainloop()
