
from PIL import Image
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Funções para manipulação do arquivo CSV
def salvar(tarefa, data_inicial, data_final, obs, prioridade):
    if os.path.exists('tarefas_fap.csv'):
        df = pd.read_csv('tarefas_fap.csv')
    else:
        df = pd.DataFrame(columns=["Tarefa", "Data Inicial", "Data Final", "Observações", "Prioridade"], )

    nova_tarefa = {
        "Tarefa": tarefa,
        "Data Inicial": data_inicial,
        "Data Final": data_final,
        "Observações": obs,
         "Prioridade": prioridade,
    }
    
    df = df._append(nova_tarefa, ignore_index=True)
    df.to_csv('tarefas_fap.csv', index=False, encoding='utf-8')

def editar_tarefa(tarefa, alteracao):
    if os.path.exists('tarefas_fap.csv'):
        df = pd.read_csv('tarefas_fap.csv')
        for index, row in df.iterrows():
            if tarefa in row['Tarefa']:
                df.at[index, 'Tarefa'] = alteracao
                df.to_csv('tarefas_fap.csv', index=False)
                return 'Alteração realizada!'
        return 'Não foi encontrado :('
    return 'Arquivo não encontrado!'

def apagar_tarefa(tarefa):
    if os.path.exists('tarefas_fap.csv'):
        df = pd.read_csv('tarefas_fap.csv')
        for index, row in df.iterrows():
            if row['Tarefa'] == tarefa:
                df = df.drop(index)
                df.reset_index(drop=True, inplace=True)
                df.to_csv('tarefas_fap.csv', index=False, encoding='utf-8')
                return 'Deleção realizada...'
        return 'Não encontrado, verifique se tudo foi digitado corretamente'
    return 'Arquivo não encontrado!'

def listar_todas_as_tarefas():
    if os.path.exists('tarefas_fap.csv'):
        df = pd.read_csv('tarefas_fap.csv')
        return df
    return pd.DataFrame(columns=["Tarefa", "Data Inicial", "Data Final", "Observações"])

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def listar_prioridade():
    
    arquivo = 'tarefas_fap.csv'
    df = pd.read_csv(arquivo)
    p1, p2, p3, p4 ,p5 = 0, 0, 0, 0, 0

    for i,s in df.iterrows():
        print(f"Tarefa: {s['Tarefa']}")
        print(f"Prioridade: {s['Prioridade']}")
        print('\n')
        if int(s['Prioridade']) == 1:
            p1 += 1
        elif int(s['Prioridade']) == 2:
            p2 += 1
        elif int(s['Prioridade']) == 3:
            p3 += 1
        elif int(s['Prioridade']) == 4:
            p4 += 1
        elif int(s['Prioridade']) == 5:
            p5 += 1
            
    lista_de_prioridade = [p1, p2, p3, p4 ,p5]
    try:      
        if sum(lista_de_prioridade)>0:
            
            x = ['1','2','3','4','5' ]
            y = lista_de_prioridade
            
            plt.bar(x, y)  # Utiliza um gráfico de barras para melhor visualização
            plt.title('Nível de prioridade')
            plt.ylabel('Quantidade')
            plt.yticks(([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
            plt.xlabel('Prioridade da tarefa')
            st.pyplot(plt)
            
            return lista_de_prioridade
    except Exception as d:
        return f'Erro ao apresentar gráfico.Tipo: {d}'
    
def _prioridade_() :
    arquivo = 'tarefas_fap.csv'
    df = pd.read_csv(arquivo)
    encontrado = False
    st.header('Procure tarefas de acordo com a prioridade')
    nivel = st.number_input('Insira o nível de prioridade: ', min_value=1, max_value=5)
    
    
    df_filtrado = df[df["Prioridade"] == nivel]        
    st.dataframe(df_filtrado)
    
    return True           
# Interface com Streamlit

def gerir_tarefas():
    st.title('Gerenciamento de Tarefas')

    menu = st.sidebar.selectbox("Escolha uma opção", ["inicio","Inserir Tarefa", "Editar Tarefa", "Listar Tarefas", "Apagar Tarefa"])

    if menu == "inicio":        
        st.markdown('**Bém vindo, qual tarefa vai fazer hoje?**')
        try:
            st.image("https://th.bing.com/th/id/OIG4.tWQMFOR_yaer3FPp7Wn0?pid=ImgGn", caption="Imagem Ilustrativa")
        except:
            print('Continue')
    
    if menu == "Inserir Tarefa":
        if menu:
            try:
                st.header("Inserir Nova Tarefa")
                prioridade = st.number_input(label='Em uma escala de 1 a 5 qual é a prioridade da tarefa? ', min_value=1, max_value=5)    
                tarefa = st.text_input('Qual é a tarefa?')
                data_inicial = st.date_input('Data de Início')
                data_final = st.date_input('Data Final')
                obs = st.text_area('Observações [opcional]', 'Sem observações')

                if st.button('Salvar Tarefa'):
                    salvar(tarefa, data_inicial.strftime('%d/%m/%Y'), data_final.strftime('%d/%m/%Y'), obs, prioridade)
                    return st.success("Tarefa salva com sucesso!")
                              
            except ValueError as d:
                print(f'Algo inválido foi digitado: {d}')
                
    elif menu == "Editar Tarefa":
        st.header("Editar Tarefa Existente")
        tarefa = st.text_input('Conteúdo/palavra/frase que está salva:')
        alteracao = st.text_input('Conteúdo que quer inserir:')

        if st.button('Editar Tarefa'):
            resultado = editar_tarefa(tarefa, alteracao)
            st.write(resultado)

    elif menu == "Listar Tarefas":
    
        try:
            df = listar_todas_as_tarefas()    
            st.header("Listas de tarefas")
            st.dataframe(df)    
            if not df.empty:
                col1,col2 =  st.columns(2)
                #st.header("Listas de tarefas")
                #st.dataframe(df)    
                with col1:
                    st.header("Análise")
                    _listar_prioridade_ = listar_prioridade()
                with col2:
                    procurar = _prioridade_()
                    
                   
        except Exception as e:
            st.write("Nenhuma tarefa encontrada.")
            st.error(f"erro: {e}")
            st.image("https://th.bing.com/th/id/OIG2.xVsXVjc4DHT5IBFB_ThB?pid=ImgGn")

    elif menu == "Apagar Tarefa":
        st.header("Apagar Tarefa")
        tarefa = st.text_input('Conteúdo/palavra/frase que está salva para apagar:')

        if st.button('Apagar Tarefa'):
            resultado = apagar_tarefa(tarefa)
            st.write(resultado)

if __name__ =='__main__':
    gerir_tarefas()
