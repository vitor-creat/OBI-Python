import customtkinter as ctk


def login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    print(usuario, senha)
    if usuario == "admin" and senha == "1234":
        resultado_login.configure(text="Login bem-sucedido!", text_color="green")
    else:
        resultado_login.configure(text="Falha no Login", text_color="red")

janela = ctk.CTk()

janela.title("Meu primeiro App")
janela.geometry("300x350")

#Label
legenda_usuario = ctk.CTkLabel(janela, text="Usuario")
legenda_usuario.pack(pady=10)



#Entry
entrada_usuario = ctk.CTkEntry(janela, placeholder_text="Digite seu usuario")
entrada_usuario.pack(pady=10)

#Label
legenda_senha = ctk.CTkLabel(janela, text="senha")
legenda_senha.pack(pady=10)

#Entry
entrada_senha = ctk.CTkEntry(janela, placeholder_text="Digite sua senha", show="*")
entrada_senha.pack(pady=10)

#button
botao = ctk.CTkButton(janela, text="Entrar", command=login)
botao.pack(pady=10)

resultado_login = ctk.CTkLabel(janela, text="")
resultado_login.pack(pady=20)

janela.mainloop()