import subprocess
import tkinter as tk
from tkinter import ttk

def abrir_perfis():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    site = site_entry.get()
    especifico = especifico_var.get()
    comecar_do_zero = comecar_do_zero_var.get()
    perfil_inicio = perfil_inicio_entry.get()

    if especifico == "Sim":
        perfis_especificos = perfis_especificos_entry.get()
        perfis = ["Profile {}".format(p.strip()) for p in perfis_especificos.split(",")]
    else:
        num_perfis = int(num_perfis_entry.get())
        if comecar_do_zero == "Sim":
            perfis = ["Profile {}".format(i) for i in range(1, num_perfis + 1)]
        else:
            perfil_inicio = int(perfil_inicio)
            perfis = ["Profile {}".format(i + perfil_inicio) for i in range(1, num_perfis + 1)]

    for perfil in perfis:
        comando = '"{}" --profile-directory="{}" {}'.format(chrome_path, perfil, site)
        subprocess.Popen(comando, shell=True)

# Cria a janela principal
root = tk.Tk()
root.title("Abrir Perfis do Chrome")

# Cria um frame
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Adiciona widgets ao frame
site_label = ttk.Label(frame, text="Site:")
site_label.grid(row=0, column=0, sticky=tk.W)
site_entry = ttk.Entry(frame, width=50)
site_entry.grid(row=0, column=1, columnspan=2)

especifico_label = ttk.Label(frame, text="Abrir Perfis Específicos:")
especifico_label.grid(row=1, column=0, sticky=tk.W)
especifico_var = tk.StringVar(value="Não")
especifico_combobox = ttk.Combobox(frame, textvariable=especifico_var, values=["Sim", "Não"])
especifico_combobox.grid(row=1, column=1, sticky=tk.W)

perfis_especificos_label = ttk.Label(frame, text="Números dos Perfis Específicos (separados por vírgula):")
perfis_especificos_label.grid(row=2, column=0, sticky=tk.W)
perfis_especificos_entry = ttk.Entry(frame, width=50)
perfis_especificos_entry.grid(row=2, column=1, columnspan=2)

num_perfis_label = ttk.Label(frame, text="Número Máximo de Perfis a serem Abertos:")
num_perfis_label.grid(row=3, column=0, sticky=tk.W)
num_perfis_entry = ttk.Entry(frame, width=10)
num_perfis_entry.grid(row=3, column=1, sticky=tk.W)

comecar_do_zero_label = ttk.Label(frame, text="Começar do Perfil 0:")
comecar_do_zero_label.grid(row=4, column=0, sticky=tk.W)
comecar_do_zero_var = tk.StringVar(value="Sim")
comecar_do_zero_combobox = ttk.Combobox(frame, textvariable=comecar_do_zero_var, values=["Sim", "Não"])
comecar_do_zero_combobox.grid(row=4, column=1, sticky=tk.W)

perfil_inicio_label = ttk.Label(frame, text="A partir de qual perfil deseja começar? (Digite o número do perfil):")
perfil_inicio_label.grid(row=5, column=0, sticky=tk.W)
perfil_inicio_entry = ttk.Entry(frame, width=10)
perfil_inicio_entry.grid(row=5, column=1, sticky=tk.W)

abrir_button = ttk.Button(frame, text="Abrir Perfis", command=abrir_perfis)
abrir_button.grid(row=6, column=0, columnspan=3, pady=10)

# Inicia o loop principal
root.mainloop()
