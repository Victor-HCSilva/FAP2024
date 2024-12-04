# Código Expandido: interface tkinter e seaborn

import tkinter as tk
from tkinter import ttk
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from sklearn.datasets import load_iris, load_wine
import matplotlib

# Configurar backend do matplotlib para usar o TkAgg
matplotlib.use('TkAgg')

# Função para carregar dados
def load_data(dataset):
    if dataset == 'Iris':
        iris = load_iris()
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['Species'] = iris.target
        df['Species'] = df['Species'].map({i: species for i, species in enumerate(iris.target_names)})
    elif dataset == 'Wine':
        wine = load_wine()
        df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
        df['Class'] = wine.target
        df['Class'] = df['Class'].map({i: cls for i, cls in enumerate(wine.target_names)})
    return df

# Função para atualizar o gráfico
def update_plot(plot_type):
    plt.clf()
    
    if plot_type == 'Histogram':
        if 'sepal length (cm)' in df.columns:
            sns.histplot(df['sepal length (cm)'])
        else:
            sns.histplot(df[df.columns[0]])  # Usar a primeira coluna se a coluna específica não existir
    elif plot_type == 'Boxplot':
        if 'Class' in df.columns:
            # Agrupar variáveis numéricas
            num_columns = df.select_dtypes(include='number').columns
            if len(num_columns) > 1:
                sns.boxplot(x='Class', y=num_columns[0], data=df)
            else:
                sns.boxplot(x='Class', y=num_columns[0], data=df)
    elif plot_type == 'Barplot':
        if 'Class' in df.columns:
            # Agrupar variáveis numéricas
            num_columns = df.select_dtypes(include='number').columns
            if len(num_columns) > 1:
                sns.barplot(x='Class', y=num_columns[0], data=df)
            else:
                sns.barplot(x='Class', y=num_columns[0], data=df)
    elif plot_type == 'Scatterplot':
        if len(df.columns) >= 2:
            sns.scatterplot(x=df.columns[0], y=df.columns[1], hue=df.columns[2] if len(df.columns) > 2 else None, data=df)
    elif plot_type == 'Heatmap':
        corr = df.select_dtypes(include='number').corr()  # Calcular a correlação entre variáveis numéricas
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    
    canvas.draw()

# Função para atualizar o conjunto de dados
def on_data_change(event):
    global df
    df = load_data(data_menu.get())
    # Atualizar o menu de gráficos para refletir que um novo conjunto de dados foi carregado
    plot_menu.set(plot_types[0])
    update_plot(plot_menu.get())

# Função para atualizar o gráfico ao selecionar um novo tipo de gráfico
def on_selection(event):
    update_plot(plot_menu.get())

# Função para fechar a aplicação
def close_app():
    root.destroy()

# Criar a janela principal
root = tk.Tk()
root.title("Seaborn Plot Viewer")

# Título
title = tk.Label(root, text="Visualizador de Gráficos", font=("Helvetica", 16))
title.pack(pady=10)

# Criar o menu lateral
menu_frame = tk.Frame(root)
menu_frame.pack(side=tk.LEFT, fill=tk.Y)

# Menu para escolher o conjunto de dados
data_menu = tk.StringVar(value='Iris')
data_dropdown = ttk.Combobox(menu_frame, textvariable=data_menu, values=['Iris', 'Wine'])
data_dropdown.pack(padx=10, pady=10)

# Opções de gráficos
plot_types = ['Histogram', 'Boxplot', 'Barplot', 'Scatterplot', 'Heatmap']
plot_menu = tk.StringVar(value=plot_types[0])
plot_dropdown = ttk.Combobox(menu_frame, textvariable=plot_menu, values=plot_types)
plot_dropdown.pack(padx=10, pady=10)

# Botão Sair
exit_button = tk.Button(menu_frame, text="Sair", command=close_app)
exit_button.pack(padx=10, pady=10)

# Configurar o gráfico
fig, ax = plt.subplots(figsize=(6, 6))  # Ajuste o tamanho do gráfico para o heatmap
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Inicializar o dataframe com a base de dados padrão
df = load_data(data_menu.get())
update_plot(plot_menu.get())

# Eventos
data_dropdown.bind('<<ComboboxSelected>>', on_data_change)
plot_dropdown.bind('<<ComboboxSelected>>', on_selection)

root.mainloop()
