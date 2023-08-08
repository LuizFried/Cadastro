import customtkinter as ctk
import tkinter as tk
import win32com.client as win32
from tkinter import messagebox


janela = tk.Tk()
janela.title('Registro')
janela.geometry('600x500')
janela.resizable(False, False)
janela.configure(background='#002368')

def mail(mail=''):
    x = 0
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

f0 = tk.Frame(janela,background='#a0ded6')
f0.grid(row=0, column=0, columnspan=3,padx=10, pady=10)

texto1 = ctk.CTkLabel(f0, text='EMAIL:',width=150, corner_radius=100,fg_color='black',text_color='white',
                      bg_color='#a0ded6', font=('Arial', 14, 'bold'))
texto1.grid(row=0, column=0, padx=2, pady=10)
teste = tk.LabelFrame(janela,text='testando')
teste.grid(row=1,column=1)

janela.mainloop()