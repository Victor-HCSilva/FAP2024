import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="user",
            password="senha",
            database="db"
        )
        
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                descricao VARCHAR(255),
                data_criacao DATE,
                data_conclusao DATE,
                responsavel VARCHAR(100),
                estado_da_tarefa TEXT
            )
        """)
        print('Olá!\n')
        return conn, cursor
    
    except mysql.connector.Error as d:
        print(f'\nErro ao conectar ao banco de dados/criar tabela: {d}')
        return None, None

def inserir_tarefa(cursor, descricao, data_criacao, data_conclusao, responsavel, estado_da_tarefa):
    cursor.execute("""
        INSERT INTO tarefas (descricao, data_criacao, data_conclusao, responsavel, estado_da_tarefa)
        VALUES (%s, %s, %s, %s, %s)
    """, (descricao, data_criacao, data_conclusao, responsavel, estado_da_tarefa))

def listar_tarefas(cursor):
    try:
        cursor.execute("SELECT * FROM tarefas")
        
        for tarefa in cursor.fetchall():
            print(tarefa)
            
    except Exception as e:
        print(f'Erro ao exibir banco de dados: {e}')

def editar_tarefa(cursor, id_tarefa, nova_descricao, nova_data_conclusao, novo_responsavel, estado_da_tarefa):
    try:
        cursor.execute("""
            UPDATE tarefas
            SET descricao = %s, data_conclusao = %s, responsavel = %s, estado_da_tarefa = %s
            WHERE id = %s
        """, (nova_descricao, nova_data_conclusao, novo_responsavel, estado_da_tarefa, id_tarefa))
        
    except Exception as d:
        print(f'Erro: {d}')

def editar_descricao(cursor, id_tarefa, nova_descricao):
    try:
        cursor.execute("""
            UPDATE tarefas
            SET descricao = %s
            WHERE id = %s
        """, (nova_descricao, id_tarefa))
    except Exception as d:
        print(f'Erro: {d}')

def editar_data_conclusao(cursor, id_tarefa, nova_data_conclusao):
    try:
        cursor.execute("""
            UPDATE tarefas
            SET data_conclusao = %s
            WHERE id = %s
        """, (nova_data_conclusao, id_tarefa))
    except Exception as d:
        print(f'Erro: {d}')

def editar_responsavel(cursor, id_tarefa, novo_responsavel):
    try:
        cursor.execute("""
            UPDATE tarefas
            SET responsavel = %s
            WHERE id = %s
        """, (novo_responsavel, id_tarefa))
    except Exception as d:
        print(f'Erro: {d}')

def editar_estado_da_tarefa(cursor, id_tarefa, estado_da_tarefa):
    try:
        cursor.execute("""
            UPDATE tarefas
            SET estado_da_tarefa = %s
            WHERE id = %s
        """, (estado_da_tarefa, id_tarefa))
    except Exception as d:
        print(f'Erro: {d}')

def excluir_tarefa(cursor, id_tarefa):
    cursor.execute("DELETE FROM tarefas WHERE id = %s", (id_tarefa,))

def main():
    try:
        conn, cursor = connect_db()
        
        while True:
            print("1. Inserir Tarefa\n2. Listar Tarefas\n3. Editar Tarefa\n4. Excluir Tarefa\n5. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                descricao = input("Descrição: ")
                data_criacao = input("Data de Criação (YYYY-MM-DD): ")
                data_conclusao = input("Data de Conclusão (YYYY-MM-DD): ")
                responsavel = input("Responsável: ")
                estado_da_tarefa = input("Estado da tarefa: ")
                inserir_tarefa(cursor, descricao, data_criacao, data_conclusao, responsavel, estado_da_tarefa)
                conn.commit()
                
            elif escolha == '2':
                listar_tarefas(cursor)
                
            elif escolha == '3':
                while True:
                    print('\n[1] Mudar toda configuração da tarefa')
                    print('[2] Mudar a descrição')
                    print('[3] Mudar a data de conclusao')
                    print('[4] Mudar responsável pela tarefa')
                    
                    mudar = input('O que deseja alterar? ')
                
                    if mudar == "1":
                        id_tarefa = input("ID da Tarefa: ")
                        nova_descricao = input("Nova Descrição: ")
                        nova_data_conclusao = input("Nova Data de Conclusão (YYYY-MM-DD): ")
                        novo_responsavel = input("Novo Responsável: ")
                        estado_da_tarefa = input("Estado da tarefa: ")
                        editar_tarefa(cursor, id_tarefa, nova_descricao, nova_data_conclusao, novo_responsavel, estado_da_tarefa)
                        conn.commit()
                        break
                        
                    elif mudar == "2":
                        id_tarefa = input("ID da Tarefa: ")
                        nova_descricao = input("Nova descrição da tarefa: ")
                        editar_descricao(cursor, id_tarefa, nova_descricao)
                        conn.commit()
                        break
                    
                    elif mudar == "3":
                        id_tarefa = input("ID da Tarefa: ")
                        nova_data_conclusao = input('Data de conclusao (YYYY-MM-DD): ')
                        editar_data_conclusao(cursor, id_tarefa, nova_data_conclusao)
                        conn.commit()
                        break
                    
                    elif mudar == "4":
                        id_tarefa = input("ID da Tarefa: ")
                        novo_responsavel = input("Novo responsável pela tarefa: ")
                        editar_responsavel(cursor, id_tarefa, novo_responsavel)
                        conn.commit()
                        break
                    else:
                        print(f'\nOpção inválida, você digitou: {mudar}')
                                    
            elif escolha == '4':
                id_tarefa = input("ID da Tarefa: ")
                excluir_tarefa(cursor, id_tarefa)
                conn.commit()
                
            elif escolha == '5':
                break
            
            else:
                print(f'\nDigite algo válido, você digitou: {escolha}')
                
        cursor.close()
        conn.close()
        
    except Exception as e: 
        print(f'\nErro no programa: {e}')               
        
    finally:
        print('\nEncerrando programa')
        
if __name__ == "__main__":
    main()
