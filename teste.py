import tkinter as tk
from tkinter import ttk, messagebox

# --------------------- DADOS EM MEMÓRIA ---------------------
clientes = []
servicos = [
    {"nome": "Corte Masculino", "valor": 35.00},
    {"nome": "Barba Completa", "valor": 25.00},
    {"nome": "Corte + Barba", "valor": 55.00},
    {"nome": "Sobrancelha", "valor": 15.00},
    {"nome": "Hidratação", "valor": 20.00}
]

atendimentos = []

# --------------------- FUNÇÕES ---------------------

def cadastrar_atendimento():
    nome = entry_nome.get()
    idade = entry_idade.get()
    servico_escolhido = combo_servico.get()

    if nome == "" or idade == "" or servico_escolhido == "":
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    try:
        idade = int(idade)
    except:
        messagebox.showerror("Erro", "Idade inválida!")
        return

    if idade < 10:
        messagebox.showerror("Erro", "Idade mínima para atendimento é 10 anos.")
        return

    # Pegando valor do serviço
    valor = None
    for s in servicos:
        if s["nome"] == servico_escolhido:
            valor = s["valor"]
            break

    atendimento = {
        "nome": nome,
        "idade": idade,
        "servico": servico_escolhido,
        "valor": valor
    }

    atendimentos.append(atendimento)
    atualizar_lista()
    messagebox.showinfo("Sucesso", "Atendimento cadastrado com sucesso!")

    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    combo_servico.set("")


def atualizar_lista():
    listbox.delete(0, tk.END)
    total = 0

    for a in atendimentos:
        texto = f"{a['nome']} | {a['servico']} | R$ {a['valor']:.2f}"
        listbox.insert(tk.END, texto)
        total += a['valor']

    label_total.config(text=f"Total do Dia: R$ {total:.2f}")


def cadastrar_servico():
    nome = entry_servico_nome.get()
    preco = entry_servico_preco.get()

    if nome == "" or preco == "":
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    try:
        preco = float(preco)
    except:
        messagebox.showerror("Erro", "Preço inválido!")
        return

    novo_servico = {"nome": nome, "valor": preco}
    servicos.append(novo_servico)

    combo_servico['values'] = [s["nome"] for s in servicos]

    messagebox.showinfo("Sucesso", "Serviço adicionado!")
    entry_servico_nome.delete(0, tk.END)
    entry_servico_preco.delete(0, tk.END)

# --------------------- INTERFACE ---------------------

janela = tk.Tk()
janela.title("Sistema de Barbearia")
janela.geometry("500x650")

titulo = tk.Label(janela, text="💈 Sistema de Barbearia", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# --------------------- CADASTRO DE ATENDIMENTO ---------------------
frame1 = tk.LabelFrame(janela, text="Cadastro de Atendimento", padx=10, pady=10)
frame1.pack(padx=10, pady=10, fill="both")

tk.Label(frame1, text="Nome do Cliente:").pack()
entry_nome = tk.Entry(frame1, width=40)
entry_nome.pack()

tk.Label(frame1, text="Idade:").pack()
entry_idade = tk.Entry(frame1, width=40)
entry_idade.pack()

tk.Label(frame1, text="Serviço:").pack()
combo_servico = ttk.Combobox(frame1, width=37, state="readonly")
combo_servico['values'] = [s["nome"] for s in servicos]
combo_servico.pack()

btn_cadastrar = tk.Button(frame1, text="Cadastrar Atendimento", bg="#4CAF50", fg="white", command=cadastrar_atendimento)
btn_cadastrar.pack(pady=10)

# --------------------- LISTA DE ATENDIMENTOS ---------------------
frame2 = tk.LabelFrame(janela, text="Atendimentos do Dia", padx=10, pady=10)
frame2.pack(padx=10, pady=10, fill="both")

listbox = tk.Listbox(frame2, width=60, height=10)
listbox.pack()

label_total = tk.Label(frame2, text="Total do Dia: R$ 0.00", font=("Arial", 12, "bold"))
label_total.pack(pady=5)

# --------------------- CADASTRO DE SERVIÇOS ---------------------
frame3 = tk.LabelFrame(janela, text="Adicionar Novo Serviço", padx=10, pady=10)
frame3.pack(padx=10, pady=10, fill="both")

tk.Label(frame3, text="Nome do Serviço:").pack()
entry_servico_nome = tk.Entry(frame3, width=40)
entry_servico_nome.pack()

tk.Label(frame3, text="Preço (R$):").pack()
entry_servico_preco = tk.Entry(frame3, width=40)
entry_servico_preco.pack()

btn_add_servico = tk.Button(frame3, text="Adicionar Serviço", bg="#2196F3", fg="white", command=cadastrar_servico)
btn_add_servico.pack(pady=10)

janela.mainloop()
