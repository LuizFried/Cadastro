import customtkinter as ctk
import tkinter as tk
import win32com.client as win32
from tkinter import messagebox


janela = tk.Tk()
janela.title('Registro')
janela.geometry('600x500')
janela.resizable(True, True)
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


frame1 = tk.Frame(janela, background='#a0ded6', width=400,height=200)
frame1.grid(padx=10, pady=10,columnspan=5)



nome = ctk.CTkLabel(frame1, text='NOME:',width=50, corner_radius=1000,fg_color='black',text_color='white',
                      bg_color='#a0ded6', font=('Arial', 12, 'bold'))
nome.grid(row=0, column=0, padx=2, pady=10)

enome = ctk.CTkEntry(frame1,width=200)
enome.grid(row=0, column=1, padx=20, pady=10)


idade = ctk.CTkLabel(frame1, text='IDADE:',width=50, corner_radius=1000,fg_color='black',text_color='white',
                      bg_color='#a0ded6', font=('Arial', 12, 'bold'))
idade.grid(row=0, column=3, padx=20, pady=10)

eidade = ctk.CTkEntry(frame1,width=35)
eidade.grid(row=0, column=4, padx=20, pady=10)


email = ctk.CTkLabel(frame1, text='EMAIL:',width=50, corner_radius=1000,fg_color='black',text_color='white',
                      bg_color='#a0ded6', font=('Arial', 12, 'bold'))
email.grid(row=3, column=0, padx=2, pady=10)

eemail = ctk.CTkEntry(frame1,width=200)
eemail.grid(row=3, column=1, padx=10, pady=10)




janela.mainloop()