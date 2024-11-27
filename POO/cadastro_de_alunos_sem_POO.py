import csv
import pandas as pd

class Aluno:
    def __init__(self, nome, matricula, curso, telefone, email):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.telefone = telefone
        self.email = email

class SistemaCadastro:
    def __init__(self, arquivo='teste.csv'):
        self.arquivo = arquivo

    def salvar(self, alunos):
        with open(self.arquivo, 'a', encoding='utf8', newline='') as arquivo:
            writer = csv.writer(arquivo)
            for aluno in alunos:
                writer.writerow([aluno.nome, aluno.matricula, aluno.curso, aluno.telefone, aluno.email])
        print('Cadastrado(a).')

    def acessar(self, nome='', matricula='0', mudanca='', tipo='', email=''):
        df = pd.read_csv(self.arquivo)

        nome = nome.lower().strip()
        matricula = str(matricula).strip()
        mudanca = mudanca.strip().lower()
        encontrado = False

        for i, row in df.iterrows():
            if row['nome'].lower().strip() == nome and str(row['matricula']).strip() == matricula:
                encontrado = True
                if tipo == '1':
                    df.at[i, 'nome'] = mudanca
                    print('\nNome atualizado!')
                elif tipo == '2':
                    df.at[i, 'matricula'] = mudanca
                    print('Matrícula atualizada!')
                elif tipo == '3':
                    df.at[i, 'curso'] = mudanca
                    print('Curso atualizado!')
                elif tipo == '4':
                    df.at[i, 'telefone'] = mudanca
                    print('Telefone atualizado!')
                elif tipo == '5':
                    df.at[i, 'email'] = mudanca
                    print('\nMudança de email realizada!')
                elif tipo == '6':
                    df = df.drop(i).reset_index(drop=True)
                    print('Deleção realizada...')
                break

        if not encontrado:
            print('\nNão foi encontrado(a), verifique se tudo foi digitado corretamente.')

        df.to_csv(self.arquivo, index=False, encoding='utf-8')
        print('Arquivo atualizado.')

    def aluno_info(self, nome='teste da silva', matricula='20230000'):
        with open(self.arquivo, mode='r', encoding='utf8') as file:
            reader = csv.reader(file)
            rows = list(reader)

        encontrado = False
        for row in rows:
            if row[0].strip().lower() == nome.lower() and row[1] == str(matricula):
                print(f'\n\nDados gerais de {nome.title()}:')
                print('------------------------------------------')
                print('Nome:', row[0])
                print('Matrícula:', row[1])
                print('Curso:', row[2])
                print('Telefone:', row[3])
                print('Email:', row[4])
                print('------------------------------------------')
                encontrado = True
                break

        if not encontrado:
            print('\nNão encontrado, verifique se tudo foi digitado corretamente')

    @staticmethod
    def informacao():
        print('\n---------------------------------------------')
        print('OPÇÕES-MENU')
        print('---------------------------------------------')
        print('[1] Para ver dados do(a) aluno(a)')
        print('[2] Para cadastrar um novo(a) aluno(a)')
        print('[3] Para deletar/alterar perfil do(a) aluno(a)')
        print('[0] Para sair')
        print('---------------------------------------------')

    @staticmethod
    def informacao2():
        print('\n---------------------------------------------')
        print('ALTERAR/DELETAR:')
        print('---------------------------------------------')
        print('[1] para alterar o nome do aluno: ')
        print('[2] para alterar matrícula')
        print('[3] para alterar curso')
        print('[4] para alterar telefone')
        print('[5] para alterar email')
        print('[6] Para deletar todos os dados de um aluno(a): ')
        print('[0] para voltar ao menu principal')
        print('---------------------------------------------')

    @staticmethod
    def informacao3():
        print('\n------------------------------------------')
        print('BUSCAR DADOS:')
        print('---------------------------------------------')
        print('[0] para ir ao menu principal: ')
        print('[1] para ver informações gerais')


if __name__ == "__main__":
    sistema = SistemaCadastro()
    cadastrar = True
    alunos = []

    while cadastrar:
        SistemaCadastro.informacao()
        escolha = input('Digite:')

        if escolha == '1':
            while True:
                SistemaCadastro.informacao3()
                escolher = input('[2] para ver dados do(a) aluno(a) em específico: ')
                if escolher == '1':
                    print('\nTabela: Alunos - Matrícula - Email:')
                    with open('teste.csv', mode='r', encoding='utf8') as file:
                        reader = csv.reader(file)
                        rows = list(reader)
                    for row in rows:
                        print('', row[0], '   -   ', row[1], '  -  ', row[4])
                elif escolher == '2':
                    nome_pesquisa = input('Insira o nome do aluno(a): ')
                    matricula_pesquisa = int(input('Insira a matrícula: '))
                    sistema.aluno_info(nome=nome_pesquisa, matricula=str(matricula_pesquisa))
                elif escolher == '0':
                    break
                else:
                    print(f'Opção inválida! Você digitou: {escolher}')

        elif escolha == '2':
            while True:
                try:
                    print('\n------------------------------------------------------')
                    print('CADASTRAR NOVO ALUNO')
                    print('------------------------------------------------------')
                    aluno_nome = input('Insira o nome: ').title()
                    aluno_matricula = int(input('Insira o número de matrícula: '))
                    aluno_curso = input('Curso do aluno(a): ').title().rstrip()
                    aluno_telefone = int(input('Insira o número de telefone: '))
                    aluno_email = input('Email do aluno(a): ')

                    aluno = Aluno(aluno_nome, aluno_matricula, aluno_curso, aluno_telefone, aluno_email)
                    alunos.append(aluno)
                    sistema.salvar(alunos)
                    alunos.remove(aluno)

                except:
                    print('\nOps, digitou alguma coisa que não podia!')
                    print('Você tem que inserir os dados novamente')

                finally:
                    break

            while True:
                mais_cadastro = input('\nRealizar outra operação (s/n)?').lower().rstrip()
                if mais_cadastro == 's':
                    break
                elif mais_cadastro == 'n':
                    cadastrar = False
                    break
                else:
                    print('\nPor favor, digite "n" se não quiser cadastrar outro aluno(a)\nou "s" se quiser cadastrar.')

        elif escolha == '3':
            while True:
                SistemaCadastro.informacao2()
                opcao = input('Digite: ')

                if opcao == '1':
                    nome = input('\nInsira o nome a ser alterado: ')
                    matricula = int(input('Insira o número de matrícula: '))
                    novo_nome = input('Insira o novo nome: ')
                    sistema.acessar(nome=nome, mudanca=novo_nome, tipo=opcao, matricula=matricula)

                elif opcao == '2':
                    nome = input('Insira o nome do aluno(a): ')
                    email_confirmar = input('Insira o email do aluno(a), por favor: ')
                    mudanca = int(input('Insira a nova matrícula: '))
                    sistema.acessar(nome=nome, mudanca=mudanca, tipo=opcao, email=email_confirmar)

                elif opcao == '3':
                    nome = input('\nInsira o nome do aluno(a): ')
                    matricula = input('Insira o número de matrícula: ')
                    curso = input('Insira o novo curso: ')
                    sistema.acessar(mudanca=curso, tipo=opcao, nome=nome, matricula=str(matricula))

                elif opcao == '4':
                    nome = input('\nInsira o nome do(a) aluno(a): ')
                    matricula = input('Insira o número de matrícula: ')
                    numero = input('Insira o novo número: ')
                    sistema.acessar(nome=nome, matricula=str(matricula), mudanca=numero, tipo=opcao)

                elif opcao == '5':
                    nome = input('\nInsira o nome do(a) aluno(a): ')
                    matricula = input('Insira o número de matrícula: ')
                    email = input('Insira o novo email: ')
                    sistema.acessar(nome=nome, matricula=str(matricula), mudanca=email, tipo=opcao)

                elif opcao == '6':
                    nome = input('Insira o nome do(a) aluno(a) para apagar os dados: ')
                    matricula = input('Insira o número de matrícula do(a) aluno(a): ')
                    sistema.acessar(mudanca='', nome=nome, matricula=str(matricula), tipo=opcao)

                elif opcao == '0':
                    break
                else:
                    print(f'Opção inválida! Você digitou {opcao}')

        elif escolha == '0':
            cadastrar = False
        else:
            print(f'Opção inválida! Você digitou "{escolha}"')

    try:
        pass
    except:
        print('Nada cadastrado!')
