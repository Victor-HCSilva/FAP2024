# Exemplo de interface gráfica usando tkinter
# Agosto de 2024 - José Alfredo Costa

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Definir um DataFrame de exemplo
data = {
    'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59],
    'tip': [1.01, 1.66, 3.50, 3.31, 3.61],
    'day': ['Sun', 'Sun', 'Sun', 'Sat', 'Sat'],
    'size': [2, 3, 3, 2, 4]
}
tips = pd.DataFrame(data)

# Função para atualizar o gráfico com base na seleção do menu
def update_graph(selected_graph):
    # Limpa o gráfico existente
    for widget in graph_frame.winfo_children():
        widget.destroy()
    
    # Gera um novo gráfico com base na seleção
    fig, ax = plt.subplots()
    
    if selected_graph == "Scatter Plot":
        sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', size='size', ax=ax)
    elif selected_graph == "Bar Chart":
        categories = ['A', 'B', 'C', 'D']
        values = [4, 7, 1, 8]
        ax.bar(categories, values)
    elif selected_graph == "Pie Chart":
        labels = ['A', 'B', 'C', 'D']
        sizes = [15, 30, 45, 10]
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    elif selected_graph == "Line Chart":
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 5, 7, 11]
        ax.plot(x, y, marker='o')
    elif selected_graph == "Histogram":
        sns.histplot(data=tips['total_bill'], kde=True, ax=ax)
    
    # Renderiza o gráfico na área de exibição
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Função para exibir o DataFrame de exemplo
def display_dataframe():
    for widget in data_frame.winfo_children():
        widget.destroy()
    
    columns = list(tips.columns)
    tree = ttk.Treeview(data_frame, columns=columns, show="headings")
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    for _, row in tips.iterrows():
        tree.insert("", "end", values=list(row))
    
    tree.pack(fill=tk.BOTH, expand=True)

# Cria a janela principal
root = tk.Tk()
root.title("Data Visualization Interface")
root.geometry("1000x600")

# Menu lateral para selecionar o tipo de gráfico
menu_frame = tk.Frame(root, width=200, bg="lightgrey")
menu_frame.pack(side="left", fill="y")

menu_label = tk.Label(menu_frame, text="Select Graph Type", bg="lightgrey")
menu_label.pack(pady=10)

graph_types = ["Scatter Plot", "Bar Chart", "Pie Chart", "Line Chart", "Histogram"]

for graph in graph_types:
    button = tk.Button(menu_frame, text=graph, command=lambda g=graph: update_graph(g))
    button.pack(fill="x", padx=10, pady=5)

# Título centralizado
title_label = tk.Label(root, text="Data Visualization", font=("Helvetica", 16))
title_label.pack(pady=10)

# DataFrame com dados de exemplo
data_frame = tk.Frame(root)
data_frame.pack(fill="x", padx=20, pady=10)
display_dataframe()

# Área de exibição do gráfico
graph_frame = tk.Frame(root)
graph_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Inicializa a interface com um gráfico de dispersão padrão
update_graph("Scatter Plot")

# Inicia a interface gráfica
root.mainloop()
