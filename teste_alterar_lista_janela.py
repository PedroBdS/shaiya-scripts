import tkinter as tk
from tkinter import messagebox
from funcoes import *
from PIL import Image, ImageTk

# Função para confirmar a alteração do valor
def confirmar_alteracao():
    try:
        valor_moedas = entry_valor.get()
        gold_novo, silver_novo, copper_novo = map(int, valor_moedas.split())
        valor_novo = gold_para_valor(gold_novo, silver_novo, copper_novo)
        atualizar_item_csv(nome_lido, valor_novo)
        messagebox.showinfo("Concluído", "Valor alterado com sucesso!")
        root.destroy()  # Fecha a janela
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao alterar valor: {e}")


# Função para abrir a janela de alteração
def abrir_janela_alteracao():
    global entry_valor

    janela_alteracao = tk.Toplevel(root)
    janela_alteracao.resizable(False, False)
    janela_alteracao.title("Alterar Valor")
    janela_alteracao.geometry("400x220+-470+380")  # Janela de 400x300 posicionada 500px à direita e 200px para baixo

    label_instrucoes = tk.Label(janela_alteracao, text="Digite o valor em ouro, prata e cobre (separados por espaço):")
    label_instrucoes.pack(pady=10)

    entry_valor = tk.Entry(janela_alteracao)
    entry_valor.pack(pady=5)

    btn_confirmar = tk.Button(janela_alteracao, text="Confirmar", command=confirmar_alteracao)
    btn_confirmar.pack(pady=10)

# Função principal para iniciar o processo
def iniciar_processo():
    global nome_lido, root

    nome_lido = ler_nome()
    valor_na_lista = int(procurar_ou_adicionar(nome_lido))
    gold, silver, copper = valor_para_gold(valor_na_lista)


    root = tk.Tk()
    root.iconbitmap("./arquivos_tkinter/shaiya.ico")
    root.title("Alteração de Valor")
    root.resizable(False, False)
    root.geometry("400x220+-470+380")  # Janela de 400x220 posicionada 470px à esquerda e 380px para baixo
    
    imagem = Image.open("./arquivos_tkinter/fundo.png")  # Use o caminho da sua imagem
    imagem_fundo = ImageTk.PhotoImage(imagem)

    label_fundo = tk.Label(root, image=imagem_fundo)
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

    texto_item = tk.Label(root, text=f'Item identifcado')
    texto_item.pack(pady=10)

    label_nome = tk.Label(root, text=f'{nome_lido}', font=("Arial", 14, "bold"))
    label_nome.place(x=75, y=39)
    # label_nome.pack(pady=10)

    label_valor = tk.Label(root, text=f'Valor: {gold}g {silver}s {copper}c')
    label_valor.pack(pady=10)

    btn_alterar = tk.Button(root, text="Alterar Valor", command=abrir_janela_alteracao)
    btn_alterar.pack(pady=10)

    root.mainloop()

# Inicia o processo
iniciar_processo()
