# interface
import tkinter as tk
from tkinter import ttk
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np

# Gerar um dataframe de exemplo
def generate_dataframe():
    data = {
        'Category': np.random.choice(['A', 'B', 'C'], size=100),
        'Value': np.random.rand(100) * 100
    }
    return pd.DataFrame(data)

df = generate_dataframe()

# Função para atualizar o gráfico
def update_plot(plot_type):
    plt.clf()
    
    if plot_type == 'Histogram':
        sns.histplot(df['Value'])
    elif plot_type == 'Boxplot':
        sns.boxplot(x='Category', y='Value', data=df)
    elif plot_type == 'Barplot':
        sns.barplot(x='Category', y='Value', data=df)
    elif plot_type == 'Scatterplot':
        sns.scatterplot(x='Category', y='Value', data=df)
    
    canvas.draw()

# Criar a janela principal
root = tk.Tk()
root.title("Seaborn Plot Viewer")

# Título
title = tk.Label(root, text="Visualizador de Gráficos", font=("Helvetica", 16))
title.pack(pady=10)

# Criar o menu lateral
menu_frame = tk.Frame(root)
menu_frame.pack(side=tk.LEFT, fill=tk.Y)

# Opções de gráficos
plot_types = ['Histogram', 'Boxplot', 'Barplot', 'Scatterplot']
plot_menu = tk.StringVar(value=plot_types[0])
plot_dropdown = ttk.Combobox(menu_frame, textvariable=plot_menu, values=plot_types)
plot_dropdown.pack(padx=10, pady=10)

# Configurar o gráfico
fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Atualizar gráfico quando a seleção mudar
def on_selection(event):
    update_plot(plot_dropdown.get())

plot_dropdown.bind('<<ComboboxSelected>>', on_selection)

# Inicializar com o gráfico padrão
update_plot(plot_dropdown.get())

root.mainloop()
