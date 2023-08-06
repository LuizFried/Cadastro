import customtkinter as tk
import win32com.client as win32
from tkinter import messagebox


janela = tk.CTk()
janela.title('Registro')
janela.geometry('600x500')
janela.resizable(True, True)
janela.configure(background='#000000')


def mail(mail=''):
    try:
        outlook = win32.Dispatch('outlook.application')
        email = outlook.CreateItem(0)


        email.To = mail
        email.Subject = "xxxxx"
        email.HTMLBody = f"""
        <p>Olá, sua senha é: {x}</p>
        
        
        <p>Abs,</p>
        <p>L.Felipe</p>
        """


        email.Send()
    except:
        messagebox.showerror('ERRO', 'Digite um email válido')





janela.mainloop()