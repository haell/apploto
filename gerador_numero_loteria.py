from random import sample
import tkinter as tk
from tkinter import messagebox

regras_jogos = {
    "Mega-sena": {"min_dezenas": 6, "max_dezenas": 15, "min_valor": 1, "max_valor": 60},
    "Quina": {"min_dezenas": 5, "max_dezenas": 15, "min_valor": 1, "max_valor": 80},
    "Lotofácil": {"min_dezenas": 15, "max_dezenas": 20, "min_valor": 1, "max_valor": 25},
    "Lotomania": {"min_dezenas": 50, "max_dezenas": 50, "min_valor": 1, "max_valor": 100},
    "Timemania": {"min_dezenas": 10, "max_dezenas": 10, "min_valor": 1, "max_valor": 80}
}

def gerar_jogos():
    opcao = opcao_var.get()
    jogos_solicitados = entry_jogos.get()
    dezenas_solicitadas = option_dezenas.get()

    if not jogos_solicitados.isdigit():
        messagebox.showerror("Erro", "Número de jogos inválido!")
        return

    jogos_solicitados = int(jogos_solicitados)

    if not regras_jogos[opcao]["min_dezenas"] <= dezenas_solicitadas <= regras_jogos[opcao]["max_dezenas"]:
        messagebox.showerror("Erro", "Número de dezenas inválido!")
        return

    resultado_text.delete(1.0, tk.END)

    for i in range(jogos_solicitados):
        jogo = sorted(sample(range(regras_jogos[opcao]["min_valor"], regras_jogos[opcao]["max_valor"] + 1), dezenas_solicitadas))
        resultado_text.insert(tk.END, f"{i+1}° Jogo => {' '.join(str(dezena) for dezena in jogo)}\n")

def atualizar_opcao(*args):
    opcao = opcao_var.get()

    if opcao == "Lotofácil":
        dezenas_frame.pack()
        option_menu_dezenas['menu'].delete(0, 'end')
        for i in range(regras_jogos[opcao]['min_dezenas'], regras_jogos[opcao]['max_dezenas'] + 1):
            option_menu_dezenas['menu'].add_command(label=i, command=lambda value=i: option_dezenas.set(value))
    else:
        dezenas_frame.pack_forget()
        option_dezenas.set(regras_jogos[opcao]['min_dezenas'])

window = tk.Tk()
window.title("Gerador de Jogos")
window.geometry("400x400")
window.resizable(False, False)
window.configure(bg="white")

label_titulo = tk.Label(window, text="Gerador de Jogos", font=("Arial", 16), bg="white")
label_titulo.pack(pady=10)

label_opcao = tk.Label(window, text="Escolha uma opção:", font=("Arial", 12), bg="white")
label_opcao.pack()

opcoes = list(regras_jogos.keys())
opcao_var = tk.StringVar(window)
opcao_var.set(opcoes[0])
option_menu_opcao = tk.OptionMenu(window, opcao_var, *opcoes)
option_menu_opcao.pack(pady=10)

dezenas_frame = tk.Frame(window, bg="white")
label_dezenas = tk.Label(dezenas_frame, text="Escolha o número de dezenas:", font=("Arial", 12), bg="white")
label_dezenas.pack()

option_dezenas = tk.IntVar(window)
option_menu_dezenas = tk.OptionMenu(dezenas_frame, option_dezenas, regras_jogos[opcoes[0]]["min_dezenas"])
option_menu_dezenas.pack(pady=10)

entry_jogos = tk.Entry(window, font=("Arial", 12))
entry_jogos.pack(pady=10)

button_gerar = tk.Button(window, text="Gerar Jogos", font=("Arial", 12), command=gerar_jogos)
button_gerar.pack(pady=10)

resultado_text = tk.Text(window, font=("Arial", 12))
resultado_text.pack(fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(resultado_text)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
resultado_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=resultado_text.yview)

# Oculta o frame de dezenas inicialmente
dezenas_frame.pack_forget()

# Vincula a função de atualizar_opcao ao evento de mudança da opção selecionada
opcao_var.trace("w", atualizar_opcao)

# Inicia a janela
window.mainloop()
